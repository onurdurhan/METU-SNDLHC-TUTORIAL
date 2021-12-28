import ROOT, sys, os, getopt
import rootUtils as ut
from decorators import *
import operator
import argparse
import math
from array import array
import sys

parser=argparse.ArgumentParser()
parser.add_argument("-f","--files",dest="inputFile",help="no help",required=True)
args=parser.parse_args()
inputFile=args.inputFile
PDG=ROOT.TDatabasePDG.Instance()
f=ROOT.TFile(inputFile)
sTree=f.cbmsim
hist={}
print("processing the file",inputFile)

ut.bookHist(hist,'xypos','x y positions of muons',100,-300,300,100,-300,300)
ut.bookHist(hist,'p','momentum distribution of muons',1000,0.,5000)
ut.bookHist(hist,'ppt','p versus pt ',1000,0.,5000,100,0.,5.) ### play with the bin size 
#ut.bookHist(hist,'weight','weight distribution',nbrofbins,0,wMax) ### assign the correct number of bins and the wMax
ut.bookHist(hist,'pbrem','momentum distribution of muons from Bremsstrahlung',1000,0.,5000)
ut.bookHist(hist,'plepton','momentum distribution of muons from pair prod.',1000,0.,5000)
ut.bookHist(hist,'compton','momentum distribution of muons from Compton',1000,0.,5000)
ut.bookHist(hist,'decay','momentum distribution of muons from decay',1000,0.,5000)

def check():
    global hist 
    for event in sTree:
        if sTree.GetReadEvent()%10000==0:print("event at ", sTree.GetReadEvent())
        for t in sTree.MCTrack:
            pdg = t.GetPdgCode()
            if abs(pdg)==13:
                x=t.GetStartX()
                y=t.GetStartY()
                p=t.GetP()
                #hist['xypos'].Fill(x,y)
                w=t.GetWeight()*2.56E7
                hist['p'].Fill(p,w)
                ##### Fill p-pt histogram here not weighted ####
                ### Fill weight distribution here ######
                procName = t.GetProcName()
                if procName == "Bremsstrahlung":
                    ##### Fill weighted & normalized histogram for Bremss.#####
                if procName == "Lepton lepton pair production"    
                if procName == 'Compton scattering':
                    ##### Fill weighted & normalized histogram for Compton
                if procName == 'Decay':
                    #### Fill weighted & normalized histogram for Decay

    return hist

rc=check()
#h1=rc['xypos']
#h2=rc['p']
#h1.SetXTitle('x[cm]')
#h1.SetYTitle('y[cm]')
#h2.SetXTitle('P(GeV/c)

#h1=weight distribution
#h2=momentum distribution of all
#h3=Brems mom.
#h4=pair prod.
#h5=compton
#h6=decay

h2.SetLineColor(2)
h3.SetLineColor(3)
h4.SetLineColor(4)
h5.SetLineColor(5)
h6.SetLineColor(6)

h3.Draw()
h4.Draw("same")
h5.Draw("same")
h6.Draw("same")

#ut.writeHists(hist,"histos.root")
#print "analysis done ","histos-"+fName, " created"
