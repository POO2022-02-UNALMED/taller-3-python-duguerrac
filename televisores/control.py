from televisores.tv import TV

class Control:
    def getTv(self):
        return self._tv

    def enlazar(self, tv):
        self._tv = tv
        self._tv._control = self

    def turnOff(self):
        self._tv._estado = False

    def turnOn(self):
        self._tv._estado = True

    def canalUp(self):
        if self._tv._estado == True:
            self._tv._canal += 1
    
    def canalDown(self):
        if self._tv._estado == True:
            self._tv._canal -= 1
    
    def volumenUp(self):
        if self._tv._estado == True:
            self._tv._volumen += 1

    def volumenDown(self):
        if self._tv._estado == True:
            self._tv._volumen -= 1
                
    def setCanal(self, canal):
        if self._tv._estado == True:
            if self._tv._canal <= 120:
                self._tv._canal = canal
