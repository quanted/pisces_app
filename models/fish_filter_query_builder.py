from .structures import CaseInsensitiveDict


class FishProperties:
    def __init__(self):
        self.attrib = CaseInsensitiveDict()
        self.attrib['scicomname'] = ''
        self.attrib['speciesid'] = ''
        self.attrib['genusid'] = ''
        self.attrib['genus'] = ''
        self.attrib['species'] = ''
        self.attrib['commonname'] = ''
        self.attrib['family'] = ''
        self.attrib['group'] = ''
        self.attrib['native'] = ''
        self.attrib['pfg_page'] = ''
        self.attrib['sportfishing'] = ''
        self.attrib['nongame'] = ''
        self.attrib['subsis_fish'] = ''
        self.attrib['pollut_tol'] = ''
        self.attrib['max_length'] = ''
        self.attrib['mean_length'] = ''
        self.attrib['mean_weight'] = ''
        self.attrib['thinning'] = ''
        self.attrib['thin_adj'] = ''
        self.attrib['max_age'] = ''
        self.attrib['w_l_a'] = ''
        self.attrib['w_l_b'] = ''
        self.attrib['l_w_c'] = ''
        self.attrib['l_w_d'] = ''
        self.attrib['regress'] = ''
        self.attrib['rarity'] = ''
        self.attrib['caves'] = ''
        self.attrib['springs'] = ''
        self.attrib['headwaters'] = ''
        self.attrib['creeks'] = ''
        self.attrib['small_riv'] = ''
        self.attrib['med_riv'] = ''
        self.attrib['lge_riv'] = ''
        self.attrib['lk_imp_pnd'] = ''
        self.attrib['swp_msh_by'] = ''
        self.attrib['coast_ocea'] = ''
        self.attrib['riffles'] = ''
        self.attrib['run_flopool'] = ''
        self.attrib['pool_bckwtr'] = ''
        self.attrib['benthic'] = ''
        self.attrib['surface'] = ''
        self.attrib['nrshre_litt'] = ''
        self.attrib['opnwtr_pelag'] = ''
        self.attrib['mud_slt_det'] = ''
        self.attrib['sand'] = ''
        self.attrib['gravel'] = ''
        self.attrib['rck_rub_bol'] = ''
        self.attrib['vegetation'] = ''
        self.attrib['wdyd_brush'] = ''
        self.attrib['clearwater'] = ''
        self.attrib['turbidwater'] = ''
        self.attrib['warmwater'] = ''
        self.attrib['coolwater'] = ''
        self.attrib['coldwater'] = ''
        self.attrib['lowlands_lgr'] = ''
        self.attrib['uplands_hgr'] = ''
        self.attrib['locat_notes'] = ''
        self.attrib['habit_notes'] = ''

    def build_query(self, query_dict):
        """
        Build a query string for filtering fish
        :param query_dict: QueryDict from the request object
        :return: query string
        """

        # Loop over keys in request dictionary, match them up to database fields
        # Build query accounting for the exceptions
        qry_sci_name = ''
        qry_common_name = ''
        qry_group = ''
        qry_native = ''
        qry_pollut_tol = ''
        qry_rarity = ''
        qry_range = ''
        qry_max_age = ''
        qry_mean_weight = ''
        qry_mean_length = ''
        qry_max_length = ''
        qry_habitat = ''

        #Used in a couple of places to remove a trailing 'or '
        trailing_or = 'or '

        for req_key, req_val in query_dict.items():
            # Is request param a valid query param
            if req_key in self.attrib:

                if (req_key.lower() == 'scientific_name'):
                    words = req_val.split(' ')
                    if len(words) == 1:
                        qry_sci_name = (" genus LIKE '%%{0}%%' or species LIKE '%%{0}%%'")
                        qry_sci_name = str.format(qry_sci_name, words[0])
                    elif len(words) == 2:
                        qry_sci_name = (" (genus LIKE '%%{0}%%' and species LIKE '%%{1}%%') or (species LIKE '%%{0}%%' and genus LIKE '%%{1}%%')")
                        qry_sci_name = str.format(qry_sci_name, words[0], words[1])

                if req_key.lower() == 'common_name':
                    words = req_val.split(' ')
                    if len(words) == 1:
                        qry_common_name = (" commonname LIKE '%%{0}%%'")
                        qry_common_name = str.format(qry_common_name, words[0])
                    elif len(words) == 2:
                        qry_sci_name = (" (commonname LIKE '%%{0}%%' and commonname LIKE '%%{1}%%')")
                        qry_sci_name = str.format(qry_sci_name, words[0], words[1])
                    elif len(words) == 3:
                        qry_sci_name = (" (commonname LIKE '%%{0}%%' and commonname LIKE '%%{1}%%' and commonname LIKE '%%{2}%%')")
                        qry_sci_name = str.format(qry_sci_name, words[0], words[1], words[2])

                    #words = req_val.split('_')
                    #if len(words) == 1:
                    #    qry_name = (" genus LIKE '%%{0}%%' or species LIKE '%%{0}%%' or commonname LIKE '%%{0}%%'")
                    #    qry_name = str.format(qry_name, words[0])
                    #elif len(words) == 2:
                    #   qry_name = (" (genus LIKE '%%{0}%%' and species LIKE '%%{1}%%') or commonname LIKE '%%{0} {1}%%'")
                    #    qry_name = str.format(qry_name, words[0], words[1])
                    #for word in words:
                    #    qry_tmp = (" genus LIKE '%%{0}%%' or species LIKE '%%{0}%%' or commonname LIKE '%%{0}%%'")
                    #    qry_tmp = str.format(qry_name, words)
                    #    qry_name = qry_name + qry_tmp + " or"

                    #if qry_name.endswith(trailing_or):
                    #    qry_name = qry_name[:-len(trailing_or)]
                    #continue


                # Can be multiple groups
                #e.g.  grp='Black Bass' or grp='Mullet'
                if (req_key.lower() == 'group'):
                    words = req_val.split(',')
                    for idx, grp in enumerate(words):
                        if idx != 0:
                            qry_group += " or "
                        qry_group += str.format(" lower(grp) = '{0}'", grp.lower())
                    continue

                if (req_key.lower() == 'native'):
                    qry_native = str.format(" native='{0}'",req_val)
                    continue

                # pollution tolerance can be: "I", "T", "M", or "U"
                if (req_key.lower() == 'pollut_tol'):
                    qry_pollut_tol = str.format(" pollut_tol='{0}'",req_val.upper())
                    continue

                if (req_key.lower() == 'rarity'):
                    range = req_val.split('_')
                    if len(range) == 2:
                        qry_rarity = str.format(" rarity>={0} and rarity<={1}", range[0], range[1])
                    continue

                if (req_key.lower() == 'max_age'):
                    range = req_val.split('_')
                    if len(range) == 2:
                        qry_max_age = str.format(" max_age>={0} and max_age<={1}", range[0], range[1])
                    continue

                if (req_key.lower() == 'mean_weight'):
                    range = req_val.split('_')
                    if len(range) == 2:
                        qry_mean_weight = str.format(" mean_weight>={0} and mean_weight<={1}", range[0], range[1])
                    continue

                if (req_key.lower() == 'mean_length'):
                    range = req_val.split('_')
                    if len(range) == 2:
                        qry_mean_length = str.format(" mean_length>={0} and mean_length<={1}", range[0], range[1])
                    continue

                if (req_key.lower() == 'max_length'):
                    range = req_val.split('_')
                    if len(range) == 2:
                        qry_max_length = str.format(" max_length>={0} and max_length<={1}", range[0], range[1])
                    continue

                #The rest of the query parameters are are used if value == 1
                #e.g. caves=1
                param = req_key.lower()
                if (req_val == '1'):
                    qry_habitat += str.format(" {0}='1' or ", param)

        #Remove trailing 'or ' from qry_habitat string
        #trailing_or = 'or '
        if qry_habitat.endswith(trailing_or):
            qry_habitat = qry_habitat[:-len(trailing_or)]

        query = "select * from fishproperties where"
        if qry_name != '':
            query += qry_name

        if qry_group != '':
            query += ' and' + qry_group

        if qry_native != '':
            query += ' and' + qry_native

        if qry_pollut_tol != '':
            query += ' and' + qry_pollut_tol

        if qry_rarity != '':
            query += ' and' + qry_rarity

        if qry_range != '':
            query += ' and' + qry_range

        if qry_max_age != '':
            query += ' and' + qry_max_age

        if qry_mean_weight != '':
            query += ' and' + qry_mean_weight

        if qry_mean_length != '':
            query += ' and' + qry_mean_length

        if qry_max_length != '':
            query += ' and' + qry_max_length

        if qry_habitat != '':
            query += ' and' + qry_habitat

        return query

