from openerp.osv.orm import except_orm


def new_init(self, name, value):
    self.name = name
    self.value = value
    # Tried `value` and `(value)` but these resulted in each character being
    # interpreted as an arg and for some reason only the first two args are
    # displayed in the error message client side.
    #
    # Also tried `(value,)` and `(value,None)` but these second args resulted
    # in `undefined` and `null` respectively being displayed client side.
    self.args = (value, '')

except_orm.__init__ = new_init
