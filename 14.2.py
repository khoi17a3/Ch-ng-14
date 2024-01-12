def nhap_so():
    so_truoc = []
    so_chan = 0
    while True:
        try:
            so = input("Nhập một số nguyên dương: ")
            if so == '0':
                break
            so = int(so)
            if so < 0:
                raise ValueError("Lỗi số âm !!!")
            if so_truoc.count(so) == 4:
                raise ValueError("Lỗi nhập lặp lại !!!")
            if so % 2 == 0:
                so_chan += 1
                if so_chan == 5:
                    raise ValueError("Lỗi nhập chẵn!!!")
            else:
                so_chan = 0
            so_truoc.append(so)
        except ValueError as e:
            print("Lỗi: ", str(e))
        except Exception:
            print("Lỗi nhập số !!!")

nhap_so()
