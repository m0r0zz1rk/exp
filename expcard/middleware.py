from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.shortcuts import HttpResponse
from django.urls import resolve
from django.utils.module_loading import import_string
from netaddr import IPAddress, IPSet
from ldap3 import Server, Connection, SIMPLE, SYNC, ASYNC, SUBTREE, ALL


def get_info_ad_from_settings(name):
    return getattr(settings, name)


def GetDataFromAD(request):
    AD_SERVER = get_info_ad_from_settings('AD_SERV')
    AD_USER = get_info_ad_from_settings('AD_US')
    AD_PASSWORD = get_info_ad_from_settings('AD_PASS')
    AD_SEARCH_TREE = get_info_ad_from_settings('AD_SEARCH')   
    server = Server(AD_SERVER)
    conn = Connection(server, user=AD_USER, password=AD_PASSWORD)
    conn.bind()
    user = request.user.username
    conn.search(AD_SEARCH_TREE, '(sAMAccountName='+user+')', SUBTREE, attributes=['DisplayName','department','mail'])
    user = conn.entries
    return [user[0].displayName, user[0].department, user[0].mail]


def get_networks_from_settings(name):
    return IPSet(getattr(settings, name, []))


def check_network(request):
    user_ip = request.META['HTTP_X_FORWARDED_FOR']
    if IPAddress(user_ip.rpartition(':')[0]) in get_networks_from_settings('ALLOWED_NETWORKS'):
        return True
    else:
        return False


class AdminWhitelistMiddleware:
    """Limits login to specific IP's in Django 3"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = resolve(request.path_info)
        is_admin_app = (current_url.app_name == 'admin')
        if is_admin_app and check_network(request) == False:
            return HttpResponse('Доступ только из внутренней сети организации')
        return self.get_response(request)