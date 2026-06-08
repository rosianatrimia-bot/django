from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import AkunSosmed
from .forms import AkunSosmedForm


PLATFORM_NAMES = {
    'instagram': 'Instagram',
    'tiktok': 'TikTok',
    'facebook': 'Facebook',
    'twitter': 'X / Twitter',
}


def home(request):
    context = {
        'page_title': 'Sosial Media',
    }
    return render(request, 'sosmed/home.html', context)


def list_sosmed(request, platform):
    keyword = request.GET.get('keyword')
    semua_akun = AkunSosmed.objects.filter(platform=platform)

    if keyword:
        semua_akun = semua_akun.filter(username__icontains=keyword)

    context = {
        'page_title': PLATFORM_NAMES.get(platform, 'Sosial Media'),
        'platform': platform,
        'semua_akun': semua_akun,
    }

    return render(request, 'sosmed/list.html', context)


def create(request, platform):
    akun_form = AkunSosmedForm(request.POST or None)

    if request.method == 'POST':
        if akun_form.is_valid():
            akun = akun_form.save(commit=False)
            akun.platform = platform
            akun.save()
            messages.success(request, 'Data berhasil disimpan')
            return redirect('sosmed:list', platform=platform)

    context = {
        'page_title': f'Tambah Akun {PLATFORM_NAMES.get(platform, "Sosial Media")}',
        'platform': platform,
        'akun_form': akun_form,
    }

    return render(request, 'sosmed/create.html', context)


def update(request, platform, update_id):
    akun_update = get_object_or_404(
        AkunSosmed,
        id=update_id,
        platform=platform
    )

    akun_form = AkunSosmedForm(
        request.POST or None,
        instance=akun_update
    )

    if request.method == 'POST':
        if akun_form.is_valid():
            akun = akun_form.save(commit=False)
            akun.platform = platform
            akun.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('sosmed:list', platform=platform)

    context = {
        'page_title': f'Update Akun {PLATFORM_NAMES.get(platform, "Sosial Media")}',
        'platform': platform,
        'akun_form': akun_form,
    }

    return render(request, 'sosmed/create.html', context)


def delete(request, platform, delete_id):
    akun_delete = get_object_or_404(
        AkunSosmed,
        id=delete_id,
        platform=platform
    )

    akun_delete.delete()
    messages.success(request, 'Data berhasil dihapus')
    return redirect('sosmed:list', platform=platform)
