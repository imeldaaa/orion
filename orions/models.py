from django.db import models

class Buku(models.Model):
    id_buku = models.AutoField(primary_key=True)
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    penerbit = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    ukuran = models.CharField(max_length=50)
    halaman = models.IntegerField()
    sinopsis = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()

    def __str__(self):
        return self.judul

class Blog(models.Model):
    id_blog = models.AutoField(primary_key=True)
    kategori = models.CharField(max_length=50)
    tanggal = models.DateField()
    penulis = models.CharField(max_length=100)
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.judul
    
class PeralatanPendidikan(models.Model):
    id_peralatan_pendidikan = models.AutoField(primary_key=True)
    nama_peralatan = models.CharField(max_length=100)
    unit = models.IntegerField()
    kategori = models.CharField(max_length=50)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()

    def __str__(self):
        return self.nama_peralatan