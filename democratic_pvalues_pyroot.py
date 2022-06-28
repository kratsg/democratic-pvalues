import math
import ROOT as r

def democraticpvalue(signifs):
    if len(signifs)!=2:
        print "More than 2 bins currently not supported."
        return 0
    p=[r.RooStats.SignificanceToPValue(signifs[0]),
       r.RooStats.SignificanceToPValue(signifs[1])]

    a=(1.-p[0])*(1.-p[1])
    return 1.-a*(1.-math.log(a))


def democraticsignif(signifs):
    return r.RooStats.PValueToSignificance(democraticpvalue(signifs))


def suminquad(signifs):
    tot=0
    for i in signifs:
        tot+=i*i
    return tot**0.5


bins=100
bmin=0.
bmax=5.

hdp0=r.TH2F("hdp0","hdp0;#sigma_{1};#sigma_{2}",bins,bmin,bmax,bins,bmin,bmax)
hsqd=r.TH2F("hsqd","hsqd;#sigma_{1};#sigma_{2}",bins,bmin,bmax,bins,bmin,bmax)
hdif=r.TH2F("hdif","hdif;#sigma_{1};#sigma_{2}",bins,bmin,bmax,bins,bmin,bmax)
for x in xrange(100):
    for y in xrange(100):

        signifs=[x*bmax/bins,
                y*bmax/bins]

        dp0=democraticsignif(signifs)
        sqd=suminquad(signifs)
        hdp0.SetBinContent(x+1,y+1,dp0)
        hsqd.SetBinContent(x+1,y+1,sqd)
        if sqd>0.:
            hdif.SetBinContent(x+1,y+1,(dp0-sqd))

cdp0=r.TCanvas("cdp0","cdp0",800,600)
hdp0.Draw("COLZ")
csqd=r.TCanvas("csqd","csqd",800,600)
hsqd.Draw("COLZ")
cdif=r.TCanvas("cdif","cdif",800,600)
hdif.Draw("COLZ")


signifs=[5.,0.5]
print democraticsignif(signifs)
print suminquad(signifs)
