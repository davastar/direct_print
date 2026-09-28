import flet as ft
import base64

def main(page: ft.Page):
    page.title = "Print Screenshot"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # Komponen UI
    img_preview = ft.Image(width=300, height=300, fit=ft.ImageFit.CONTAIN)
    
    def print_to_rawbt(e):
        base64_data = print_btn.data
        if base64_data:
            # Bungkus base64 ke dalam HTML agar RawBT otomatis merender gambarnya
            html_content = f'<img src="data:image/jpeg;base64,{base64_data}" width="100%">'
            # Panggil intent RawBT
            page.launch_url(f"rawbt:{html_content}")

    print_btn = ft.ElevatedButton(
        text="Cetak via RawBT", 
        icon=ft.icons.PRINT, 
        on_click=print_to_rawbt, 
        disabled=True
    )

    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            file_path = e.files[0].path
            
            # Tampilkan preview gambar
            img_preview.src = file_path
            
            # Konversi file gambar ke Base64
            with open(file_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            
            # Simpan data base64 ke tombol dan aktifkan tombol
            print_btn.data = encoded_string
            print_btn.disabled = False
            page.update()

    # Inisialisasi File Picker
    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    pick_btn = ft.ElevatedButton(
        text="Pilih Screenshot", 
        icon=ft.icons.IMAGE, 
        on_click=lambda _: file_picker.pick_files(allow_multiple=False)
    )

    page.add(
        ft.Text("Aplikasi Cetak Screenshot", size=20, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        pick_btn,
        img_preview,
        print_btn
    )

ft.app(target=main)
