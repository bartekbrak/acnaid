class StoresDbRouter(object):
    """This ensures that all dbmodel operations save to one(oliprox) db.
    Make sure oliprox db is definde in local settings"""
    app = 'stores'
    db = 'oliprox'

    def db_for_read(self, model, **hints):
        "Point all operations on myapp models to self.db"
        if model._meta.app_label == self.app:
            return self.db
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on myapp models to self.db"
        if model._meta.app_label == self.app:
            return self.db
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in myapp is involved"
        if obj1._meta.app_label == self.app or obj2._meta.app_label == self.app:
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the myapp app only appears on the self.db db"
        if db == self.db:
            return model._meta.app_label == self.app
        elif model._meta.app_label == self.app:
            return False
        return None
