class Building():


    def __init__(self, season_in_year, apartment_number, apartment_size):
        self.season_in_year = season_in_year
        self.apartment_number = apartment_number
        self.apartment_size = apartment_size

    def rent_calculation(self):
        base_price_per_month = 2000
        season_price_buffer = 0

        if self.season_in_year == "summer":
            season_price_buffer = 1.5

        elif self.season_in_year == "winter":
            season_price_buffer = 1.1

        elif self.season_in_year == "spring":
            season_price_buffer = 1.4
        else:
            season_price_buffer = 1.3


        if self.apartment_size > 130:
            season_price_buffer += 0.1

        # String Formatting !
        print("The buffer is %s" %season_price_buffer)

        total_rent_price = base_price_per_month * season_price_buffer
        print("Total rent for %s for apartment number %s. Apartment size is : %s" %(total_rent_price, self.apartment_number , self.apartment_size))

        return total_rent_price



    def monthly_maintenance_pay(self, rent_total_price):

        maintenance = 0

        if rent_total_price > 2500:
            maintenance = 100

        else:
            maintenance = 50
        print("Maintenance is %s" % maintenance)




lease_contract_1 = Building("summer", 4, 135)

total_rent_price_1 = lease_contract_1.rent_calculation()
lease_contract_1.monthly_maintenance_pay(total_rent_price_1)

print("\n")

lease_contract_2 = Building("spring", 1, 50)

total_rent_price_2 = lease_contract_2.rent_calculation()
lease_contract_2.monthly_maintenance_pay(total_rent_price_2)

