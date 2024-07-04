from .entities.site import Site

class ModelSite:

    @classmethod
    def get_sites(self, db):
        try:
            sites_list = []
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_all_sites")
            sites = cursor.fetchall()
            for i in range(len(sites)):
                sites_list.append(Site(
                    sites[i][0],
                    sites[i][1],
                    sites[i][2],
                    sites[i][3]
                ))
            cursor.close()
            return sites_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_site_by_id(self, db, site_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_site_by_id(%s)", (site_id,))
            site = cursor.fetchone()
            cursor.close()
            return Site(
                site[0],
                site[1],
                site[2],
                site[3]
            )
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_site(self, db, site):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_add_site(%s, %s, %s)", (
                site.site_name,
                site.site_address,
                site.site_region_id
            ))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_site(self, db, site):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_site(%s, %s, %s, %s)", (
                site.site_id,
                site.site_name,
                site.site_address,
                site.site_region_id
            ))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_site(self, db, site_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_site(%s)", (site_id,))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def verify_region(self, db, site_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_verify_region(%s)", (site_id,))
            region = cursor.fetchone()
            cursor.close()
            return str(region[0])
        except Exception as ex:
            raise Exception(ex)

