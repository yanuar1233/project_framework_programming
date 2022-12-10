from django.shortcuts import render
from landingpage.forms import FromBarang
from landingpage.models import Barang,Jenis,Ikan,JenisIkan

#Create your views here

def tambah_barang(request):
    form =FromBarang()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)

def barang_view(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs': barangs,
    }

    return render(request,'tampil_brg.html',konteks)

def barang_view_zen(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs': barangs,
    }

    return render(request,'zen/zen_table.html',konteks)

def uts_view(request):
    ikans=Ikan.objects.all()

    konteks={
        'ikans': ikans
    }

    return render(request,'uts/index.html',konteks)

def jenis_ikan(request):
    jenis = JenisIkan.objects.all()

    konteks={
        'jenis' : jenis
    }

    return render(request,'uts/jenis.html',konteks)