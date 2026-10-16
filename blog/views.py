from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F

from django.views import generic


class SearchView(generic.ListView):
    template_name = 'blog_list.html'
    context_object_name = 'blog'
    model = models.Blog

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context




# def blog_search_view(request):
#     query = request.GET.get('q', '')
#     if query:
#         blog = models.Blog.objects.filter(title__icontains=query)
#     else:
#         return HttpResponse('Блог не найден')
#     return render(request, 'blog_list.html', {'blog': blog})





class BlogListView(generic.ListView):
    template_name = 'blog_list.html'
    model = models.Blog
    paginate_by = 2
    ordering = ['-id']
    context_object_name = 'blog'

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = context['page_obj']
        return context




# def blog_list_view(request):
#     if request.method == 'GET':
#         blog = models.Blog.objects.all()
#         paginator_blog = Paginator(blog, 2)
#         page = request.GET.get('page')
#         page_obj = paginator_blog.get_page(page)
#     return render(request, 'blog_list.html', {'blog': page_obj})


class BlogDetailView(generic.DetailView):
    template_name = 'blog_detail.html'
    context_object_name = 'blog_id'
    pk_url_kwarg = 'id'
    model = models.Blog

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_blog = request.session.get('viewed_blog', [])

        if obj.pk not in views_blog:
            self.model.objects.filter(pk=obj.pk).update(views=F('views')+1)
            views_blog.append(obj.pk)
            request.session['views_blog'] = views_blog
            obj.refresh_from_db()
        return obj
#



# def blog_detail_view(request, id):
#     if request.method == 'GET':
#         blog_id = get_object_or_404(models.Blog, id=id)
#         views_blog = request.session.get('viewed_blog', [])
#         if id not in views_blog:
#             blog_id.views = F("views") + 1
#             blog_id.save()
#             blog_id.refresh_from_db()
#         views_blog.append(id)
#         request.session['viewed_blog'] = views_blog
#     return render(request, 'blog_detail.html', {'blog_id': blog_id})







class HelloWorldView(generic.View):
    def get(self, request):
        return HttpResponse('Ура это первый мой проект на DJANGO')


# def hello_world_view(request):
#     if request.method == "GET":
#         return HttpResponse('Ура это первый мой проект на DJANGO')

class MyFavouriteEmodjiView(generic.View):
    def get(self, request):
        return HttpResponse('😁🤣🤖🫠🌚')
    
# def my_favourite_emodji_view(request):
#     if request.method == "GET":
#         return HttpResponse('😁🤣🤖🫠🌚')

class AboutMySelfView(generic.View):
    def get(self, request):
        return HttpResponse('Меня зовут Радомир, я BACKEND DEVELOPER')

# def about_my_self_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Меня зовут Радомир, я BACKEND DEVELOPER')