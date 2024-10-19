import requests
import sys
import pyfiglet
import time
from termcolor import colored

# Define an extensive list of common admin panel paths (1000+)
admin_paths = [
    'admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/', 
    'usuario/', 'administrator/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 
    'admin_area/', 'panel-administracion/', 'instadmin/', 'memberadmin/', 'adm/', 'adminaccount/', 
    'admcp/', 'cp/', 'adminlogin/', 'siteadmin/', 'admin/admin.php', 'controlpanel/', 'backend/', 'auth/', 
    'dashboard/', 'moderator/', 'login/', 'login/admin/', 'admincp.php', 'admcp.php', 'cpanel/', 'secure_admin/', 
    'adminpanel/', 'administrator/login/', 'adminpanel.asp', 'adminpanel.php', 'admin/', 'secure/', 'admin_control/', 
    'sysadmin/', 'admin/admin-login.php', 'webadmin/admin/', 'root/admin/', 'admin/admin_login.php', 'adminaccess/', 
    'secure_adminpanel/', 'adminsection/', 'staff_login/', 'administratorlogin/', 'adminpanel.html', 'admin-interface/', 
    'manager/', 'management/', 'cms/admin/', 'adminpage/', 'adminpanel/login/', 'adminsection/', 'admin-portal/', 
    'control_panel/', 'login_panel/', 'useradmin/', 'securelogin/', 'sysadminlogin/', 'authadmin/', 'controladmin/', 
    'admin-console/', 'moderator/login/', 'webmaster/', 'rootadmin/', 'staffadmin/', 'securecontrol/', 'administrator/', 
    'admin_area.html', 'administratorlogin.asp', 'admin_controlpanel/', 'webcpanel/', 'login/admincp/', 'cms-login/', 
    'userpanel/', 'member-login/', 'memberadminpanel/', 'modcp/', 'admincp.asp', 'login_admin/', 'managementpanel/', 
    'systemadmin/', 'usercontrol/', 'paneladmin/', 'member_login/', 'admincontrol/', 'admininterface/', 'admininterface.asp', 
    'loginadmin.asp', 'admincp/', 'admininterface.html', 'adminpanel.jsp', 'serveradmin/', 'admin_login.aspx', 'webadminpanel/', 
    'controlpanel.php', 'moderatorinterface/', 'admincpanel.php', 'admincontrol.asp', 'login-admin/', 'panel/', 
    'admin_dashboard/', 'auth_login/', 'webmasteradmin/', 'moderator/admin/', 'adminsystem/', 'rootadminpanel/', 
    'controlpanel/', 'adminconsole/', 'sysadmincontrol/', 'adm.php', 'adminpanel.cfm', 'admin/admincpanel.php', 
    'systemadmin.asp', 'authlogin/', 'adminpanel.asp', 'admin_console.asp', 'web_admin/', 'admin/secure_login/', 
    'admin_section/', 'admin_tools/', 'secure-login/admin/', 'superadmin/', 'admin_section/', 'syscpanel/', 'web-login/', 
    'admin_tools_login/', 'admin_security/', 'login_cp/', 'admin_dashboard_login/', 'admin_panel.php', 'admin_account/', 
    'admin_main/', 'cms_loginpanel/', 'webmaster_login/', 'adminlogin.asp', 'controladminpanel/', 'admin-console.php', 
    'user_admin/', 'sys_admin_panel/', 'root_login/', 'administratorpanel/', 'admin_cms/', 'admin_account/', 
    'login/control_panel/', 'sysadmin_dashboard/', 'rootcpanel/', 'cpanel-login/', 'management_login/', 'admin/adminpanel.asp', 
    'login/admin_panel/', 'securepanel/', 'sysadmincp/', 'admin_login.jsp', 'admin_login_form/', 'cpanelinterface/', 
    'adminloginpage/', 'admin_cpanel/', 'adminpanel_login.asp', 'panel_admin/', 'system_console/', 'admin_portal/', 
    'adminconsole.php', 'web_admin_dashboard/', 'syslogin/', 'cmsadminpanel/', 'servercpanel/', 'admin_console/', 
    'control/admin/', 'login_admin_panel/', 'adminpanelcp/', 'admin_controlpanel/', 'admin_access/', 'serveradminlogin/', 
    'rootadmincontrol/', 'login_control/', 'admincpanel_login/', 'management/admin/', 'paneladmincp/', 'auth_admin/', 
    'cms-admin/', 'userpaneladmin/', 'cpanel/admincp/', 'moderatorcontrol/', 'secure_access/', 'userlogin/', 'cms_control/', 
    'adminconsolepanel/', 'root_control/', 'admininterfaceadmin/', 'cmsloginpanel/', 'admin_area_login/', 'web/admincp/', 
    'admin_dashboard_control/', 'login_dashboard/', 'sysadmininterface/', 'webcontrolpanel/', 'adminpagecp/', 'adminpanel_main/', 
    'root-admin/', 'rootinterface/', 'adminpanel_interface/', 'admin_portal_login/', 'sys_admin_control/', 'admin_login_admin/', 
    'admin_login_console/', 'adminpanel_access/', 'webpanelcp/', 'control_access/', 'admin_control_login/', 'userconsole/', 
    'management_dashboard/', 'admincontrol_login/', 'controlroot/', 'admincontrol_cp/', 'adminpage_login/', 'controlcpanel/', 
    'cpanelinterface_admin/', 'login_system/', 'sys_admin_dashboard/', 'root_dashboard/', 'adminpage_access/', 'cms_admin_cp/', 
    'adminlogin_dashboard/', 'administrator_access/', 'rootcp/', 'login/admincpanel/', 'userpanel_login/', 'login_admininterface/', 
    'webcpanel_dashboard/', 'rootlogincontrol/', 'cms_control_panel/', 'adminpanel_dashboard/', 'management_console/', 
    'adminpanel_login_admin/', 'admincpanel_main/', 'admin_access_control/', 'admin_panel_interface/', 'management/admincpanel/', 
    'serverlogin_admin/', 'adminpanelcontrol_admin/', 'adminpanel_cpanel/', 'root_admincontrol/', 'admincpanel_access/', 
    'rootlogin_admin/', 'sysadmincpanel/', 'adminsection_login/', 'controlpanel_login/', 'root_login_panel/', 'useradmin_login/', 
    'sys_admin_login/', 'webmaster_dashboard/', 'server_admincontrol/', 'cms_admin_dashboard/', 'admininterface_dashboard/', 
    'sysadmin_login_dashboard/', 'rootadmin_login_control/', 'admin_console_control/', 'adminpage_dashboard/', 'control_login_panel/', 
    'admin_interface_cp/', 'adminlogin_cp/', 'user_admin_dashboard/', 'adminpanel_login_cp/', 'login_webadmin/', 'login_access_control/', 
    'server_admin_dashboard/', 'user_console_cp/', 'admin_cp_dashboard/', 'cpanel_login_admin/', 'servercpanel_dashboard/', 
    'admincontrol_dashboard/', 'login_cms_admin/', 'webadmincp/', 'userpanel_dashboard/', 'sysadmin_cpanel_login/', 
    'login_admin_console/', 'server_control_panel/', 'login_rootadmin/', 'root_login_dashboard/', 'cpanel_admin_dashboard/', 
    'login_panel_dashboard/', 'control_access_admin/', 'cms_admin_interface/', 'serverlogin_dashboard/', 'syslogin_admin/', 
    'management_control/', 'adminaccess_cp/', 'adminsection_login_admin/', 'adminlogin_access/', 'sysadmin_panel/', 
    'webadmin_login/', 'cpanel_admin_interface/', 'admin_tools_control/', 'login_cpanel/', 'webmasterlogin_dashboard/', 
    'admin_console_interface/', 'adminsection_console/', 'login_serveradmin/', 'root_console_admin/', 'cms_panel_login/', 
    'sysadmininterface_dashboard/', 'login_admin_access/', 'rootpanel_dashboard/', 'sys_admin_access/', 'admincontrol_interface/', 
    'server_login_access/', 'adminpanel_root/', 'sysadminpanel_control/', 'management_login_access/', 'rootpanel_access/', 
    'cms_access_dashboard/', 'adminpanel_console_dashboard/', 'user_control_access/', 'management_admin_panel/', 'cmscontrol_admin/', 
    'server_access_admin/', 'login_admin_login/', 'admin_tools_login_control/', 'admin_interface_panel/', 'adminpanel_control_access/', 
    'control_login_admin/', 'syslogin_control_panel/', 'admin_login_cms/', 'adminpage_panel/', 'cms_login_dashboard/', 
    'managementpanel_login/', 'admin_interface_dashboard/', 'serverlogin_cpanel/', 'rootcontrol_dashboard/', 'admincpanel_interface/', 
    'login_control_dashboard/', 'login_admin_login_interface/', 'cms_dashboard_control/', 'rootlogin_dashboard_admin/', 
    'adminpanel_webadmin/', 'admin_access_dashboard/', 'admincontrol_server/', 'admin_login_webadmin/', 'login_controlpanel_admin/', 
    'adminlogin_interface_admin/', 'adminconsole_login_dashboard/', 'root_adminpanel_dashboard/', 'admincpanel_login_access/', 
    'login_control_admin_dashboard/', 'adminlogin_control_dashboard/', 'serverpanel_control/', 'admincpanel_login_admin_access/', 
    'webpanel_login_admin/', 'admincontrol_dashboard_login/', 'adminpanel_dashboard_login_admin/', 'server_admin_login_access/'
]

def dark_world_banner():
    # Create an animated banner for "DARK WORLD"
    banner_text = "DARK WORLD"
    ascii_banner = pyfiglet.figlet_format(banner_text)
    for char in ascii_banner:
        print(colored(char, 'red'), end='', flush=True)
        time.sleep(0.01)  # Speed of the animation
    print("\n" + "-"*60)

def find_admin_panel(url):
    if not url.startswith("http"):
        url = "http://" + url

    print(f"[*] Scanning website for admin panels: {url}\n")

    for path in admin_paths:
        target_url = f"{url}/{path}"
        try:
            response = requests.get(target_url)
            if response.status_code == 200:
                print(f"[✔] Admin panel found: {target_url}")
            else:
                print(f"[✘] Not found: {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"[✘] Error accessing {target_url}: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python dkadmin.py https://www.example.com")
        sys.exit(1)

    dark_world_banner()  # Display the banner before starting
    target_url = sys.argv[1]
    find_admin_panel(target_url)

if __name__ == "__main__":
    main()
