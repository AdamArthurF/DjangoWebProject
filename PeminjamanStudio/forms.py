from django import forms
from .models import *


class DataForm(forms.ModelForm):
    class Meta:
        model = DataPeminjamanStudio
        fields = ['nama',
                  'nim',
                  'jenis_kelamin',
                  'program_studi',
                  'angkatan',
                  'hari',
                  'tanggal',
                  'tempat',
                  'waktu']
        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'id': 'Nama',
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama',
                }
            ),
            'nim': forms.TextInput(
                attrs={
                    'id': 'NIM',
                    'class': 'form-control',
                    'placeholder': 'Masukkan NIM',
                }
            ),
            'jenis_kelamin': forms.Select(
                attrs={
                    'id': 'NIM',
                    'class': 'custom-select',
                }
            ),
            'program_studi': forms.Select(
                attrs={
                    'id': 'ProgramStudi',
                    'class': 'custom-select',
                }
            ),
            'angkatan': forms.Select(
                attrs={
                    'id': 'Angkatan',
                    'class': 'custom-select',
                }
            ),
            'hari': forms.TextInput(
                attrs={
                    'id': 'Hari',
                    'class': 'form-control',
                    'placeholder': 'Masukkan hari'
                }
            ),
            'tanggal': forms.TextInput(
                attrs={
                    'id': 'Tanggal',
                    'class': 'form-control',
                    'placeholder': 'Masukkan Tanggal'
                }
            ),
            'tempat': forms.TextInput(
                attrs={
                    'id': 'Tempat',
                    'class': 'form-control',
                    'placeholder': 'Masukkan Tempat'
                }
            ),
            'waktu': forms.TextInput(
                attrs={
                    'id': 'Waktu',
                    'class': 'form-control',
                    'placeholder': 'Masukkan Waktu'
                }
            ),
        }
        labels = {
            'nama': 'Nama ',
            'nim': 'NIM ',
            'jenis_kelamin': 'Jenis Kelamin ',
            'program_studi': 'Program Studi ',
            'angkatan': 'Angkatan ',
            'hari': 'Hari ',
            'tanggal': 'Tanggal ',
            'tempat': 'Tempat ',
            'waktu': 'Waktu ',
        }
