def checkCats(CatsTuti, CatsNining):
    kucing_tuti = CatsTuti
    del kucing_tuti[0]
    del kucing_tuti[-2:]
    
    data_umur_kucing = kucing_tuti + CatsNining

    for i, umur in enumerate(data_umur_kucing, start=1):
        if umur >= 3:
            print(f"Kucing nomor {i} adalah Kucing Dewasa dan berusia {umur} tahun")
        else:
            print(f"Kucing nomor {i} masih anak-anak")


print("Data Uji 1")
data_tuti1 = [3, 5, 2, 12, 7]
data_nining1 = [4, 1, 15, 8, 3]
checkCats(data_tuti1, data_nining1)

print("\nData Uji 2")
data_tuti2 = [9, 16, 6, 8, 3]
data_nining2 = [10, 5, 6, 1, 4]
checkCats(data_tuti2, data_nining2)
