import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime

# Load data dari file Excel
df = pd.read_excel('Daftar Karyawan.xlsx')

# Fungsi untuk menentukan generasi berdasarkan Tanggal Lahir
def get_generation(birthdate_str):
    try:
        birthdate = datetime.strptime(str(birthdate_str), '%Y-%m-%d')
        year = birthdate.year
        if year <= 1964:
            return 'Boomers'
        elif year >= 1965 and year <= 1980:
            return 'Gen X'
        elif year >= 1981 and year <= 1996:
            return 'Gen Y'
        elif year >= 1997 and year <= 2012:
            return 'Gen Z'
        elif year >= 2013:
            return 'Alpha'
    except (ValueError, TypeError):
        return 'Unknown'

# Menambahkan kolom Generasi ke DataFrame
df['Generasi'] = df['Tanggal Lahir'].apply(get_generation)

# Aplikasi Streamlit
st.title('Aplikasi Visualisasi Data Karyawan')

menu = st.sidebar.selectbox('Pilih Menu', ['Visualisasi Jenis Kelamin','Visualisasi Agama','Visualisasi Status Pernikahan','Visualisasi Daerah','Visualisasi Jenjang','Visualisasi Generasi'])

if menu == 'Visualisasi Jenis Kelamin':
    submenu_options = [
        'Semua', 'Jabatan', 'Unit Kerja', 'Direktorat', 'Departemen', 
        'Fungsi Jabatan', 'Kelompok Jabatan', 'Seksi', 'Job', 'Cluster'
    ]
    submenu = st.selectbox('Pilih Visualisasi Berdasarkan', submenu_options)
    
    if submenu == 'Semua':
        st.header(f'Visualisasi Jenis Kelamin untuk Semua Kategori')
        
        # Menghitung jumlah jenis kelamin untuk semua kategori
        gender_count_all = df['Jenis Kelamin'].value_counts()
        
        # Plot pie chart untuk semua kategori
        fig = px.pie(values=gender_count_all, names=gender_count_all.index, 
                     title=f'Distribusi Jenis Kelamin untuk Semua Kategori',
                     labels={'names': 'Jenis Kelamin', 'values': 'Jumlah'},
                     hole=0.3)
        
    else:
        st.header(f'Visualisasi Jenis Kelamin Berdasarkan {submenu}')
        
        # Dropdown untuk memilih kategori yang dipilih di submenu
        category_list = df[submenu].dropna().unique().tolist()
        
        # Text box untuk mencari kategori
        search_category = st.text_input(f'Cari {submenu}', '')
        if search_category:
            filtered_category_list = [cat for cat in category_list if search_category.lower() in cat.lower()]
            if filtered_category_list:
                selected_category = st.selectbox(f'Pilih {submenu} dari Hasil Pencarian', filtered_category_list)
            else:
                st.warning(f'Tidak ditemukan hasil untuk pencarian "{search_category}"')
                st.stop()
        else:
            selected_category = st.selectbox(f'Pilih {submenu}', category_list)
        
        # Filter data berdasarkan kategori yang dipilih
        filtered_df = df[df[submenu] == selected_category]
        
        # Menghitung jumlah jenis kelamin
        gender_count = filtered_df['Jenis Kelamin'].value_counts()
        
        # Plot menggunakan plotly untuk efek animasi
        fig = px.pie(values=gender_count, names=gender_count.index, 
                     title=f'Distribusi Jenis Kelamin untuk {submenu} {selected_category}',
                     labels={'names': 'Jenis Kelamin', 'values': 'Jumlah'},
                     hole=0.3)
    
    # Menambahkan layout dan animasi (opsional)
    fig.update_layout(transition_duration=500)
    
    # Tampilkan plot di Streamlit
    st.plotly_chart(fig)

#############################################################################################################
if menu == 'Visualisasi Agama':
    submenu_options = [
        'Semua', 'Jabatan', 'Unit Kerja', 'Direktorat', 'Departemen', 
        'Fungsi Jabatan', 'Kelompok Jabatan', 'Seksi', 'Job', 'Cluster'
    ]
    submenu = st.selectbox('Pilih Visualisasi Berdasarkan', submenu_options)
    
    if submenu == 'Semua':
        st.header(f'Visualisasi Agama untuk Semua Kategori')
        
        # Menghitung jumlah agama untuk semua data
        religion_count_all = df['Agama'].value_counts()
        
        # Plot pie chart untuk semua kategori
        fig = px.pie(values=religion_count_all, names=religion_count_all.index, 
                     title=f'Distribusi Agama untuk Semua Kategori',
                     labels={'names': 'Agama', 'values': 'Jumlah'},
                     hole=0.3)
        
    else:
        st.header(f'Visualisasi Agama Berdasarkan {submenu}')
        
        # Dropdown untuk memilih kategori yang dipilih di submenu
        category_list = df[submenu].dropna().unique().tolist()
        
        # Text box untuk mencari kategori
        search_category = st.text_input(f'Cari {submenu}', '')
        if search_category:
            filtered_category_list = [cat for cat in category_list if search_category.lower() in cat.lower()]
            if filtered_category_list:
                selected_category = st.selectbox(f'Pilih {submenu} dari Hasil Pencarian', filtered_category_list)
            else:
                st.warning(f'Tidak ditemukan hasil untuk pencarian "{search_category}"')
                st.stop()
        else:
            selected_category = st.selectbox(f'Pilih {submenu}', category_list)
        
        # Filter data berdasarkan kategori yang dipilih
        filtered_df = df[df[submenu] == selected_category]
        
        # Menghitung jumlah agama
        religion_count = filtered_df['Agama'].value_counts()
        
        # Menentukan jenis chart berdasarkan submenu
        if submenu in ['Cluster', 'Kelompok Jabatan', 'Direktorat']:
            # Plot menggunakan plotly untuk efek animasi
            fig = px.bar(x=religion_count.index, y=religion_count.values, 
                         labels={'x': 'Agama', 'y': 'Jumlah'},
                         title=f'Distribusi Agama untuk {submenu} {selected_category}')
        else:
            # Plot menggunakan plotly untuk efek animasi
            fig = px.pie(values=religion_count, names=religion_count.index, 
                         title=f'Distribusi Agama untuk {submenu} {selected_category}',
                         labels={'names': 'Agama', 'values': 'Jumlah'},
                         hole=0.3)
    
    # Menambahkan layout dan animasi (opsional)
    fig.update_layout(transition_duration=500)
    
    # Tampilkan plot di Streamlit
    st.plotly_chart(fig)

#############################################################################################################

if menu == 'Visualisasi Status Pernikahan':
    submenu_options = [
        'Semua', 'Jabatan', 'Unit Kerja', 'Direktorat', 'Departemen', 
        'Fungsi Jabatan', 'Kelompok Jabatan', 'Seksi', 'Job', 'Cluster'
    ]
    submenu = st.selectbox('Pilih Visualisasi Berdasarkan', submenu_options)
    
    if submenu == 'Semua':
        st.header(f'Visualisasi Status Pernikahan untuk Semua Kategori')
        
        # Menghitung jumlah status pernikahan untuk semua data
        marriage_status_count_all = df['Status Pernikahan'].value_counts()
        
        # Plot pie chart untuk semua kategori
        fig = px.pie(values=marriage_status_count_all, names=marriage_status_count_all.index, 
                     title=f'Distribusi Status Pernikahan untuk Semua Kategori',
                     labels={'names': 'Status Pernikahan', 'values': 'Jumlah'},
                     hole=0.3)
        
    else:
        st.header(f'Visualisasi Status Pernikahan Berdasarkan {submenu}')
        
        # Dropdown untuk memilih kategori yang dipilih di submenu
        category_list = df[submenu].dropna().unique().tolist()
        
        # Text box untuk mencari kategori
        search_category = st.text_input(f'Cari {submenu}', '')
        if search_category:
            filtered_category_list = [cat for cat in category_list if search_category.lower() in cat.lower()]
            if filtered_category_list:
                selected_category = st.selectbox(f'Pilih {submenu} dari Hasil Pencarian', filtered_category_list)
            else:
                st.warning(f'Tidak ditemukan hasil untuk pencarian "{search_category}"')
                st.stop()
        else:
            selected_category = st.selectbox(f'Pilih {submenu}', category_list)
        
        # Filter data berdasarkan kategori yang dipilih
        filtered_df = df[df[submenu] == selected_category]
        
        # Menghitung jumlah status pernikahan
        marriage_status_count = filtered_df['Status Pernikahan'].value_counts()
        
        # Menentukan jenis chart berdasarkan submenu
        if submenu in ['Cluster', 'Kelompok Jabatan', 'Direktorat']:
            # Plot menggunakan plotly untuk efek animasi
            fig = px.bar(x=marriage_status_count.index, y=marriage_status_count.values, 
                         labels={'x': 'Status Pernikahan', 'y': 'Jumlah'},
                         title=f'Distribusi Status Pernikahan untuk {submenu} {selected_category}')
        else:
            # Plot menggunakan plotly untuk efek animasi
            fig = px.pie(values=marriage_status_count, names=marriage_status_count.index, 
                         title=f'Distribusi Status Pernikahan untuk {submenu} {selected_category}',
                         labels={'names': 'Status Pernikahan', 'values': 'Jumlah'},
                         hole=0.3)
    
    # Menambahkan layout dan animasi (opsional)
    fig.update_layout(transition_duration=500)
    
    # Tampilkan plot di Streamlit
    st.plotly_chart(fig)


#############################################################################################################

if menu == 'Visualisasi Daerah':
    submenu_options = [
        '10 Besar', 'Jabatan', 'Unit Kerja', 'Direktorat', 'Departemen', 
        'Fungsi Jabatan', 'Kelompok Jabatan', 'Seksi', 'Job', 'Cluster'
    ]
    submenu = st.selectbox('Pilih Visualisasi Berdasarkan', submenu_options)
    
    if submenu == '10 Besar':
        st.header(f'Visualisasi Tempat Lahir Teratas')
        
        # Menghitung top 10 tempat lahir terbanyak
        top_birthplaces = df['Tempat Lahir'].value_counts().nlargest(10)
        
        # Filter data hanya untuk top 10 tempat lahir
        filtered_df = df[df['Tempat Lahir'].isin(top_birthplaces.index)]
        
        # Plot histogram untuk top 10 tempat lahir
        fig = px.histogram(filtered_df, x='Tempat Lahir', 
                           title='Histogram Distribusi Tempat Lahir untuk 10 Teratas')
        
    else:
        st.header(f'Visualisasi Tempat Lahir Berdasarkan {submenu}')
        
        # Dropdown untuk memilih kategori yang dipilih di submenu
        category_list = df[submenu].dropna().unique().tolist()
        
        # Text box untuk mencari kategori
        search_category = st.text_input(f'Cari {submenu}', '')
        if search_category:
            filtered_category_list = [cat for cat in category_list if search_category.lower() in cat.lower()]
            if filtered_category_list:
                selected_category = st.selectbox(f'Pilih {submenu} dari Hasil Pencarian', filtered_category_list)
            else:
                st.warning(f'Tidak ditemukan hasil untuk pencarian "{search_category}"')
                st.stop()
        else:
            selected_category = st.selectbox(f'Pilih {submenu}', category_list)
        
        # Filter data berdasarkan kategori yang dipilih
        filtered_df = df[df[submenu] == selected_category]
        
        # Menghitung top 10 tempat lahir terbanyak dalam kategori yang dipilih
        top_birthplaces = filtered_df['Tempat Lahir'].value_counts().nlargest(10)
        
        # Filter data hanya untuk top 10 tempat lahir dalam kategori yang dipilih
        filtered_df = filtered_df[filtered_df['Tempat Lahir'].isin(top_birthplaces.index)]
        
        # Plot histogram untuk top 10 tempat lahir dalam kategori yang dipilih
        fig = px.histogram(filtered_df, x='Tempat Lahir', 
                           title=f'Histogram Distribusi Tempat Lahir untuk {submenu} {selected_category}')
    
    # Menambahkan layout dan animasi (opsional)
    fig.update_layout(transition_duration=500)
    
    # Tampilkan plot di Streamlit
    st.plotly_chart(fig)



#############################################################################################################

if menu == 'Visualisasi Jenjang':
    submenu_options = [
        'Semua', 'Jabatan', 'Unit Kerja', 'Direktorat', 'Departemen', 'Seksi'
    ]
    submenu = st.selectbox('Pilih Visualisasi Berdasarkan', submenu_options)
    
    st.header(f'Visualisasi Jenjang Berdasarkan {submenu}')
    
    if submenu == 'Semua':
        # Menghitung jumlah jenjang untuk semua data
        level_count_all = df['Jenjang'].value_counts()
        
        # Plot histogram untuk semua data
        fig = px.histogram(x=df['Jenjang'], 
                           labels={'x': 'Jenjang', 'y': 'Jumlah'},
                           title=f'Distribusi Jenjang untuk Semua Data')
    else:
        # Dropdown untuk memilih kategori yang dipilih di submenu
        category_list = df[submenu].dropna().unique().tolist()
        
        # Text box untuk mencari kategori
        search_category = st.text_input(f'Cari {submenu}', '')
        if search_category:
            filtered_category_list = [cat for cat in category_list if search_category.lower() in cat.lower()]
            if filtered_category_list:
                selected_category = st.selectbox(f'Pilih {submenu} dari Hasil Pencarian', filtered_category_list)
            else:
                st.warning(f'Tidak ditemukan hasil untuk pencarian "{search_category}"')
                st.stop()
        else:
            selected_category = st.selectbox(f'Pilih {submenu}', category_list)
        
        # Filter data berdasarkan kategori yang dipilih
        filtered_df = df[df[submenu] == selected_category]
        
        # Menghitung jumlah jenjang
        level_count = filtered_df['Jenjang'].value_counts()
        
        # Menentukan jenis chart berdasarkan submenu
        if submenu in ['Cluster', 'Kelompok Jabatan', 'Direktorat']:
            # Plot menggunakan plotly untuk efek animasi
            fig = px.bar(x=level_count.index, y=level_count.values, 
                         labels={'x': 'Jenjang', 'y': 'Jumlah'},
                         title=f'Distribusi Jenjang untuk {submenu} {selected_category}')
        else:
            # Plot menggunakan plotly untuk efek animasi
            fig = px.pie(values=level_count, names=level_count.index, 
                         title=f'Distribusi Jenjang untuk {submenu} {selected_category}',
                         labels={'names': 'Jenjang', 'values': 'Jumlah'},
                         hole=0.3)
    
    # Menambahkan layout dan animasi (opsional)
    fig.update_layout(transition_duration=500)
    
    # Tampilkan plot di Streamlit
    st.plotly_chart(fig)


#############################################################################################################

if menu == 'Visualisasi Generasi':
    submenu_options = [
        'Semua', 'Jabatan', 'Unit Kerja', 'Direktorat', 'Departemen', 'Seksi'
    ]
    submenu = st.selectbox('Pilih Visualisasi Berdasarkan', submenu_options)
    
    st.header(f'Visualisasi Generasi Berdasarkan {submenu}')
    
    if submenu == 'Semua':
        # Menghitung jumlah generasi untuk semua data
        generation_count_all = df['Generasi'].value_counts()
        
        # Plot pie chart untuk semua data
        fig = px.pie(values=generation_count_all, names=generation_count_all.index, 
                     title=f'Distribusi Generasi untuk Semua Data',
                     labels={'names': 'Generasi', 'values': 'Jumlah'},
                     hole=0.3)
    else:
        # Dropdown untuk memilih kategori yang dipilih di submenu
        category_list = df[submenu].dropna().unique().tolist()
        
        # Text box untuk mencari kategori
        search_category = st.text_input(f'Cari {submenu}', '')
        if search_category:
            filtered_category_list = [cat for cat in category_list if search_category.lower() in cat.lower()]
            if filtered_category_list:
                selected_category = st.selectbox(f'Pilih {submenu} dari Hasil Pencarian', filtered_category_list)
            else:
                st.warning(f'Tidak ditemukan hasil untuk pencarian "{search_category}"')
                st.stop()
        else:
            selected_category = st.selectbox(f'Pilih {submenu}', category_list)
        
        # Filter data berdasarkan kategori yang dipilih
        filtered_df = df[df[submenu] == selected_category]
        
        # Menghitung jumlah generasi
        generation_count = filtered_df['Generasi'].value_counts()
        
        # Plot menggunakan plotly untuk efek animasi
        fig = px.pie(values=generation_count, names=generation_count.index, 
                     title=f'Distribusi Generasi untuk {submenu} {selected_category}',
                     labels={'names': 'Generasi', 'values': 'Jumlah'},
                     hole=0.3)
    
    # Menambahkan layout dan animasi (opsional)
    fig.update_layout(transition_duration=500)
    
    # Tampilkan plot di Streamlit
    st.plotly_chart(fig)
