################################################################################
#       _____ _                 _           _                  _               #
#      / ____(_)               | |         | |                | |              #
#     | (___  _ _ __ ___  _   _| | __ _  __| | ___  _ __    __| | ___          #
#      \___ \| | '_ ` _ \| | | | |/ _` |/ _` |/ _ \| '__|  / _` |/ _ \         #
#      ____) | | | | | | | |_| | | (_| | (_| | (_) | |    | (_| |  __/         #
#     |_____/|_|_| |_| |_|\__,_|_|\__,_|\__,_|\___/|_|     \__,_|\___|         #
#       _____           _          _______   _  __  __      _                  #
#      / ____|         | |        |__   __| (_)/ _|/_/     (_)                 #
#     | |    _   _ _ __| |_ ___      | |_ __ _| |_ __ _ ___ _  ___ ___         #
#     | |   | | | | '__| __/ _ \     | | '__| |  _/ _` / __| |/ __/ _ \        #
#     | |___| |_| | |  | || (_) |    | | |  | | || (_| \__ \ | (_| (_) |       #
#      \_____\__,_|_|   \__\___/     |_|_|  |_|_| \__,_|___/_|\___\___/        #
#                                                                              #
################################################################################
#Versão 1.0                                                                    #
#Data:24/06/2019                                                               #
#Autores: Ricardo Macedo e Antonio Galiza                                      #
#Contatos: angacego(at)gmail(dot)com                                           #
################################################################################
#        Script que contém as funções das trasnformadas de Clarke e Park       #
################################################################################
from numpy import sin,cos,matrix,sqrt,pi
from math import atan2

def converte(curtoMono,curtoBi,curtoBiTerra,curtoTri,faseAAB,faseBAC,faseCBC):
    resposta = [0,0,0,0]
    if curtoMono or curtoBi or curtoBiTerra or curtoTri:
        resposta[0]=1
        if curtoMono:
            resposta[1]=0
        elif curtoBi or curtoBiTerra:
            resposta[1]=1
            if curtoBiTerra:
                resposta[3]=1
        elif curtoTri:
            resposta[1]=2

        if faseAAB:
            resposta[2]=0
        elif faseCBC:
            resposta[2]=1
        else:
            resposta[2]=2
    else:
        return resposta
    return resposta

def curtos(xa,xb,xc, tipo, fases, terra):
    if tipo == 0:
        xa = {0:0, 1:xa, 2:xa}[fases]
        xb = {0:xb, 1:0, 2:xb}[fases]
        xc = {0:xc, 1:xc, 2:0}[fases]

    elif tipo == 1:
        if terra:
            xa = {0:0, 1:0, 2:xa}[fases]
            xb = {0:0, 1:xb,2:0}[fases]
            xc = {0:xc, 1:0, 2:0}[fases]
        else:
            xa1 = {0:(xa+xb)/2,1:(xa+xc)/2,2:xa}[fases]
            xb1 = {0:(xa+xb)/2,1:xb,2:(xb+xc)/2}[fases]
            xc1 = {0:xc,1:(xa+xc)/2,2:(xb+xc)/2}[fases]
            xa=xa1
            xb=xb1
            xc=xc1
    else:
        xa, xb, xc = 0, 0, 0
    return (xa, xb, xc)


def abc2alfabeta0(xa,xb,xc):
    vetorFases = matrix([[xa],[xb],[xc]])
    matrizClarke = 2/3*matrix([[1,-1/2,-1/2], #veio da página da Mathworks (Matlab)
                              [0,sqrt(3)/2,-sqrt(3)/2],
                              [1/sqrt(2),1/sqrt(2),1/sqrt(2)],])
    vetorAlfaBeta0 = matrizClarke*vetorFases
    return(float(vetorAlfaBeta0[0][0]),float(vetorAlfaBeta0[1][0]),float(vetorAlfaBeta0[2][0]))

def abc2dq0(xa,xb,xc,t,omega,theta):
    vetorFases = matrix([[xa],[xb],[xc]])
    matrizPark =  2/3*matrix([[cos(omega*t+theta),cos(omega*t+theta),cos(omega*t+theta)],
                                 [-sin(omega*t+theta),-sin(omega*t+theta),-sin(omega*t+theta),],
                                 [.5,.5,.5]])
    vetordq0 = matrizPark*vetorFases
    return (float(vetordq0[0][0]),float(vetordq0[1][0]),float(vetordq0[2][0]))

def alfabeta02dq0(xalfa,xbeta,x0,t,omega,theta):
    vetorClarke = matrix([[xalfa],[xbeta],[x0]])
    matrizAlfaBetaDQ0 =matrix([[cos(theta+omega*t), sin(theta+omega*t),0],[-sin(theta+omega*t),cos(theta+omega*t),0],[0,0,1]])
    vetordq0 = matrizAlfaBetaDQ0*vetorClarke
    return (float(vetordq0[0][0]),float(vetordq0[1][0]),float(vetordq0[2][0]))

def dq02abc(xd,xq,x0,t,omega,theta):
    vetorPark = matrix([[xd],[xq],[x0]])
    matrizDQ0ABC = matrix([[cos(omega*t+theta),-sin(omega*t+theta),sqrt(.5)],
                           [cos(omega*t+theta-2*pi/3),-sin(omega*t+theta-2*pi/3),sqrt(.5)],
                           [cos(omega*t+theta+2*pi/3),-sin(omega*t+theta+2*pi/3),sqrt(.5)]])
    vetorABC = matrizDQ0ABC*vetorPark
    return (float(vetorABC[0][0]),float(vetorABC[1][0]),float(vetorABC[2][0]))

def dq02alfabeta(xalfa,xbeta,x0,t):pass

def alfabeta02abc(xalfa,xbeta,x0,t):pass
