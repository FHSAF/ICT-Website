from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import BlogsModel, BodyModel, CommentModel, ReplyCommentModel, Packages
from .forms import NewCommentForm, ReplyForm
from accounts.models import UserProfile

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    blogs = BlogsModel.objects.order_by(
        '-created_at').filter(is_published=True)[:3]
    comment_count = {}
    for blog in blogs:
        comment_count[blog.id] = CommentModel.objects.filter(
            related_blog=blog.id).count()
    context = {
        'blogs': blogs,
        'comment_count': comment_count
    }
    return render(request, 'pages/index.html', context)


def BlogDetails(request, blog_id):
    blogs = BlogsModel.objects.order_by(
        '-created_at').filter(is_published=True)
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    blog_post = get_object_or_404(BlogsModel, pk=blog_id)
    body = BodyModel.objects.filter(blog=blog_id)
    comment_count = CommentModel.objects.filter(related_blog=blog_id).count()
    comments = CommentModel.objects.order_by(
        '-last_updated').filter(related_blog=blog_id)
    latest = BlogsModel.objects.order_by(
        '-created_at').filter(is_published=True)[:3]

    context = {
        'blog': blog_post,
        'latest_blogs': latest,
        'paragraphs': body,
        'comment_count': comment_count,
        'comments': comments,
        'blogs': paged_blogs

    }

    return render(request, 'pages/single.html', context)


def Blog_New_Comment(request, blog_id):
    blog_page = get_object_or_404(BlogsModel, pk=blog_id)

    if request.method == "POST":
        comment = request.POST['message']
        user_id = request.POST['user_id']
        user = get_object_or_404(UserProfile, pk=user_id)
        CommentModel.objects.create(
            comment_text=comment,
            related_blog=blog_page,
            commented_by=user
        )

        # ReplyCommentModel.objects.create(
        #     comment_text=form.cleaned_data.get('message'),
        #     comment=comment,
        #     created_by=request.user
        # )
        # return redirect('blog-details', pk=pk, comment_pk=comment.pk)
        return redirect('/{}'.format(blog_id))
    else:
        form = NewcommentForm()
    return render(request, 'Form/comment_form.html', {'blog': blog_page, 'form': form})


def comment_posts(request, pk, comment_pk):
    comment = get_object_or_404(comment, blogsmodel__pk=pk, pk=comment_pk)
    comment.views += 1
    comment.save()
    return render(request, 'comment_posts.html', {'comment': comment})


@login_required
def reply_comment(request, pk, comment_pk):
    comment = get_object_or_404(CommentModel, blog_page__pk=pk, pk=comment_pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.comment = comment
            post.created_by = request.user
            post.save()
            return redirect('comment_posts', pk=pk, comment_pk=comment_pk)
    else:
        form = ReplyForm()
    return render(request, 'reply_comment.html', {'comment': comment, 'form': form})


def Package_View(request):
    packages = Packages.objects.all()
    context = {
        'packages': packages
    }
    return render(request, 'pages/packages.html', context)
