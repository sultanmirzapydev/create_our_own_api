from django.db import models

class DataModel(models.Model):
    
    egcs = models.CharField(max_length=200,null=True,  blank=True, default=None)
    ercs = models.CharField(max_length=200,null=True, blank=True, default=None)
    erAtt =  models.FloatField( blank=True, default=None,null=True)
    erInv =  models.FloatField( blank=True, default=None,null=True)
    erUnq =  models.FloatField( blank=True, default=None,null=True)
    erLop =  models.FloatField( blank=True, default=None,null=True)
    erLmt =  models.FloatField( blank=True, default=None,null=True)
    ecAtt =  models.FloatField( blank=True, default=None,null=True)
    ecBsy =  models.FloatField( blank=True, default=None,null=True)
    ecCng =  models.FloatField( blank=True, default=None,null=True)
    ecCon =  models.FloatField( blank=True, default=None,null=True)
    ecMin =  models.FloatField( blank=True, default=None,null=True)
    ecPDD =  models.FloatField( blank=True, default=None,null=True)
    ecAsr =  models.FloatField( blank=True, default=None,null=True)
    ecAcd =  models.FloatField( blank=True, default=None,null=True)
    erChg =  models.FloatField( blank=True, default=None,null=True)
    ecChg =  models.FloatField( blank=True, default=None,null=True)
    mrgn =  models.FloatField( blank=True, default=None,null=True)
    mpct =  models.FloatField( blank=True, default=None, null=True)

    def __str__(self):
        return str(self.ercs)