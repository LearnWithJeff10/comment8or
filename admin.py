from django.contrib import admin

class Comment8orAdminSite(admin.AdminSite):
    title_header = "Comment8or Admin"
    site_header="Comment8or administration"
    index_title="Comment8or site admin"
    logout_template = "comment8or/logged_out.html"

admin_site = Comment8orAdminSite(name='comment8or')