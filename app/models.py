# Site Model
class Site(db.Model):
    __tablename__ = 'site'

    site_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_region_id = db.Column(db.Integer, db.ForeignKey('regions.region_id'), nullable=False)
    site_name = db.Column(db.String(128), nullable=False)
    site_segment = db.Column(db.Integer, nullable=False)

    region = db.relationship('Region', backref=db.backref('site', lazy=True))

    def __repr__(self):
        return f'<Site {self.site_name}>'

    def to_dict(self):
        return {
            'site_id': self.site_id,
            'fk_region_id': self.fk_region_id,
            'site_name': self.site_name,
            'site_segment': self.site_segment
        }

    def add_site(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update_site(self):
        db.session.commit()
        return self

    def delete_site(self):
        db.session.delete(self)
        db.session.commit()
        return self

    @staticmethod
    def get_all_sites():
        return Site.query.all()

    @staticmethod
    def get_site_by_id(site_id):
        return Site.query.filter_by(site_id=site_id).first()

    @staticmethod
    def get_site_by_name(site_name):
        return Site.query.filter_by(site_name=site_name).first()
# Site Model


# Session Information Model
class SessionInformation(db.Model):
    __tablename__ = 'session_information'

    session_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_ip = db.Column(db.String(16), nullable=False)
    session_mac = db.Column(db.String(32), nullable=False)
    session_username = db.Column(db.String(128), nullable=False)
    session_password = db.Column(db.String(128), nullable=False)
    api_ssl_port = db.Column(db.Integer, nullable=False)
    allow_scan = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<SessionInformation {self.session_id}>'

    def to_dict(self):
        return {
            'session_id': self.session_id,
            'session_ip': self.session_ip,
            'session_mac': self.session_mac,
            'session_username': self.session_username,
            'session_password': self.session_password,
            'api_ssl_port': self.api_ssl_port,
            'allow_scan': self.allow_scan
        }

    def add_session_information(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update_session_information(self):
        db.session.commit()
        return self

    def delete_session_information(self):
        db.session.delete(self)
        db.session.commit()
        return self

    @staticmethod
    def get_all_session_information():
        return SessionInformation.query.all()

    @staticmethod
    def get_session_information_by_id(session_id):
        return SessionInformation.query.filter_by(session_id=session_id).first()
# Session Information Model


# Router Model
class Router(db.Model):
    __tablename__ = 'router'

    router_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    router_name = db.Column(db.String(128), nullable=False)
    router_description = db.Column(db.String(256), nullable=False)
    router_brand = db.Column(db.String(128), nullable=False)
    fk_site_id = db.Column(db.Integer, db.ForeignKey('site.site_id'), nullable=False)
    fk_session_id = db.Column(db.Integer, db.ForeignKey('session_information.session_id'), nullable=False)

    site = db.relationship('Site', backref=db.backref('router', lazy=True))
    session_information = db.relationship('SessionInformation', backref=db.backref('router', lazy=True))

    def __repr__(self):
        return f'<Router {self.router_name}>'

    def to_dict(self):
        return {
            'router_id': self.router_id,
            'router_name': self.router_name,
            'router_description': self.router_description,
            'router_brand': self.router_brand,
            'fk_site_id': self.fk_site_id,
            'fk_session_id': self.fk_session_id
        }
# Router Model


# IP Address Model
class IPAddress(db.Model):
    __tablename__ = 'ip_address'

    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_router_id = db.Column(db.Integer, db.ForeignKey('router.router_id'), nullable=False)
    address_alias = db.Column(db.String(128), nullable=False)
    address_state = db.Column(db.String(4), nullable=False)
    address_ip = db.Column(db.String(16), nullable=False)
    address_netmask = db.Column(db.String(4), nullable=False)
    address_interface = db.Column(db.String(128), nullable=False)
    address_network = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return f'<IPAddress {self.address_alias}>'

    def to_dict(self):
        return {
            'address_id': self.address_id,
            'fk_router_id': self.fk_router_id,
            'address_alias': self.address_alias,
            'address_state': self.address_state,
            'address_ip': self.address_ip,
            'address_netmask': self.address_netmask,
            'address_interface': self.address_interface,
            'address_network': self.address_network
        }
# IP Address Model


# ARP List Model
class ARPList(db.Model):
    __tablename__ = 'arp_list'

    arp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_router_id = db.Column(db.Integer, db.ForeignKey('router.router_id'), nullable=False)
    arp_state = db.Column(db.String(4), nullable=False)
    arp_ip = db.Column(db.String(16), nullable=False)
    arp_mac = db.Column(db.String(32), nullable=False)
    arp_interface = db.Column(db.String(128), nullable=False)
    arp_netbios = db.Column(db.String(128), nullable=False)
    arp_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<ARPList {self.arp_ip}>'

    def to_dict(self):
        return {
            'arp_id': self.arp_id,
            'fk_router_id': self.fk_router_id,
            'arp_state': self.arp_state,
            'arp_ip': self.arp_ip,
            'arp_mac': self.arp_mac,
            'arp_interface': self.arp_interface,
            'arp_netbios': self.arp_netbios,
            'arp_date': self.arp_date
        }
# ARP List Model
