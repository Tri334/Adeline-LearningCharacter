import numpy as np
import random


train_0 = "train/o.txt"
train_x = 'train/x.txt'

test_01 = "test/o1.txt"
test_02 = "test/o2.txt"

test_x1 = "test/x1.txt"
test_x2 = "test/x2.txt"

w = [0.2, 0.5, 0.3, 0.4, 0.6, 0.8, 0.9, 0.5, 0.7, 0.27, 0.36, 0.65, 0.25, 0.96, 0.46, 0.66, 0.34, 0.46, 0.61, 0.21, 0.33, 0.45, 0.71, 0.69, 0.88]

b = 0.4
a = 0.2
batas = 0.2

t0 = -1.0
tx = 1.0


# print(f"{type(w)}\n"
#       f"{type(b)}\n"
#       f"{type(a)}\n"
#       f"{type(t0)}\n")


#Membaca file dan dirubah ke array
def parsing(file):
    f0 = open(file, "r")
    file = f0.read()
    f0.close()
    file = file.replace("\n",'')
    return file

#Mengubah setiap item menjadi -1 dan 1 berdasarkan rule yang ada
def preprocesing(file):
    file = parsing(file)
    file = [-1 if x is '.' else 1 for x in file]
    return file

#Mencari v
def hitungV(w,b,data):
    v = np.array([])
    bobot = 0
    datates = preprocesing(data)
    for i in range(len(datates)):
            bobot = w[i] * datates[i]
            v = np.append(v,bobot)
    y = np.sum(v)
    y = np.round(y,3) + b
    return y


#Menemukan Testing
def testing(v):
    if v >= 0:
        return 1
    else:
        return -1

def train(w,b,t,a,data,batas):
    p = 0
    datates = preprocesing(data)
    kondisi = False
    ab = 0
    wlama = w
    wbaru = []
    bias_baru = 0
    bias_lama = b

    x = 0
    v = 0
    while kondisi == False:
        ab +=1
        perubahan_bobot = []
        bobot_baru = []
        if bias_baru == 0:
            y = hitungV(wlama, bias_lama, data)

        elif bias_baru != 0:
            y = hitungV(wbaru,bias_baru,data)

        for i in range(len(datates)):
            bobot = (a * (t - (y)) * datates[i])
            p = wlama[i] + bobot
            wbaru.append(round(p,3))
            perubahan_bobot.append(round(bobot,3))
        bias_baru = bias_lama + (a * (t - y))
        bias_baru = round(bias_baru, 3)

        # print(f"epoch: {ab}")
        # print(f"{wbaru}")
        # print(f"max perubahan bobot: {max(perubahan_bobot)}")
        # print(f"bias baru : {bias_baru}")
        # print(f" v = {y}")

        #cek jika max perubahan bobot
        if max(perubahan_bobot) > batas:
            kondisi = False
            bias_lama = bias_baru
            wlama = wbaru
            bobot_baru = perubahan_bobot
        elif max(perubahan_bobot) < batas:
            kondisi = True
            v = hitungV(wbaru,bias_baru,data)
            hasil = print(f"Epoch yang diperlukan: {ab}\n" \
                    f"Output Testing: {testing(v)}\n" \
                    # f"v = {v}\n"\
                    f"Bobot maksimal: {max(perubahan_bobot)}")
            if testing(v) == -1:
                print(f"Output dari perceptron adalah huruf “O” \n")
            elif testing(v)== 1:
                print(f"Output dari perceptron adalah huruf “X” \n")



    return hasil

# coba = train(w,b,t0,a,train_0,batas)
# n = preprocesing(test_01)
# n2 = preprocesing(test_x2)
# print(coba)

print(f"Target Bipolar\n"
      f"Huruf O = -1\n"
      f"Huruf X = 1\n")

print(f"Uji data dengan bobot tidak random dimana\n"
      f"Bias = {b}\n"
      f"Alpha = {a}\n"
      f"Threshold = {batas}\n"
      f"Bobot = {w}\n")

print(f"Uji data O1.txt")
tes0 = train(w,b,t0,a,test_01,batas)

print(f"Uji data O2.txt")
tes2 = train(w,b,t0,a,test_02,batas)

print(f"Uji data X1.txt")
tes3 = train(w,b,tx,a,test_x1,batas)

print(f"Uji data X2.txt")
tes4 = train(w,b,tx,a,test_x2,batas)

print("====Uji data dengan bobot, bias, dan alpha random====\n")

def ujiRandom(datao1,datao2,datax1,datax2,batas):
    pengujian = 0
    while pengujian < 5:
        pengujian +=1
        print(f"Pengujian ke: {pengujian}")
        w_random = []
        for i in range(25):
            bilangan_asal = random.uniform(0, 1)
            w_random.append(bilangan_asal)
        bias_random = random.uniform(0,1)
        alpha_random = random.uniform(0,1)
        # print(len(w_random))
        # print(f"bias: {bias_random}")
        # print(f"alpha: {alpha_random}\n")

        print(f"Uji data O1.txt")
        train(w_random,bias_random,t0,alpha_random,test_01,batas)

        print(f"Uji data O2.txt")
        train(w_random,bias_random,t0,alpha_random,test_02,batas)

        print(f"Uji data X1.txt")
        train(w_random,bias_random,tx,alpha_random,test_x1,batas)

        print(f"Uji data X2.txt")
        train(w_random,bias_random,tx,alpha_random,test_x2,batas)

ujiRandom(test_01,test_02,test_x1,test_x2,batas)