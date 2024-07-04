from .entities.region import Region


class ModelRegion:

    @classmethod
    def get_regions(self, db):
        try:
            regions_list = []
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_all_regions")
            regions = cursor.fetchall()
            for i in range(len(regions)):
                regions_list.append(Region(
                    regions[i][0],
                    regions[i][1]
                ))
            cursor.close()
            return regions_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_region_by_id(self, db, region_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_region_by_id(%s)", (region_id,))
            region = cursor.fetchone()
            cursor.close()
            return Region(
                region[0],
                region[1]
            )
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_region(self, db, region):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_add_region(%s)", (
                region.region_name,))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_region(self, db, region):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_region(%s, %s)", (
                region.region_id,
                region.region_name))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_region(self, db, region_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_region(%s)", (region_id,))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)