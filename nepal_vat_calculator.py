print ('please enter YES or No')

annual_taxable_purchases_goods=0
annual_taxable_sales_goods=0
annual_taxable_services_you_purchased=0
annual_taxable_services_you_provided=0
annual_taxable_purchase_Goods_Services=0
annual_taxable_sales_Goods_Services=0



Goods_Services= input ('Do you supply both taxable goods and taxable services?:')
Goods_Services= Goods_Services.upper()

if Goods_Services == 'YES':
    annual_taxable_sales_Goods_Services= (float(input('enter your annual turnover from goods and services you provided to your client :')))
    Output_Vat=(annual_taxable_sales_Goods_Services * 13/100)
    print(f'Output_Vat={Output_Vat:.2f}')
    annual_taxable_purchase_Goods_Services=(float(input('enter your total annual purchase costs of goods and services :')))
    Input_Vat =(annual_taxable_purchase_Goods_Services  * 13/100)
    print(f'Input_Vat={Input_Vat:.2f}')
    if Output_Vat >  Input_Vat:
        print (f'Vat Payable to government ={Output_Vat - Input_Vat:.2f}')
    elif Output_Vat ==  Input_Vat:
        print ('No VAT payable or receivable ')
    else:
        print(f'Vat Receivable from government ={ Input_Vat - Output_Vat:.2f}')
else:
    Goods=input('Do you supply taxable goods?:')
    Goods= Goods.upper()
    if Goods == 'YES':
        annual_taxable_sales_goods= (float(input('enter your annual turnover from sale_of_taxable_goods:')))
        Output_Vat=(annual_taxable_sales_goods * 13/100)
        print(f'Output_Vat={Output_Vat:.2f}')
        annual_taxable_purchases_goods=(float(input('enter your total annual purchase costs of taxable goods for resale:')))
        Input_Vat =(annual_taxable_purchases_goods  * 13/100)
        print(f'Input_Vat={Input_Vat:.2f}')
        if Output_Vat >  Input_Vat:
            print (f'Vat Payable to government ={Output_Vat - Input_Vat:.2f}')
        elif Output_Vat ==  Input_Vat:
            print ('No VAT payable or receivable ')
        else:
            print(f'Vat Receivable from government ={ Input_Vat - Output_Vat:.2f}')
    else:
        Services=input('Do you supply taxable services?:')
        Services= Services.upper()
        if Services == 'YES':
            annual_taxable_services_you_provided= (float(input('enter your annual turnover from services you provided to your client :')))
            Output_Vat=(annual_taxable_services_you_provided * 13/100)
            print(f'Output_Vat={Output_Vat:.2f}')
            annual_taxable_services_you_purchased=(float(input('enter your total annual purchase costs of services :')))
            Input_Vat =(annual_taxable_services_you_purchased  * 13/100)
            print(f'Input_Vat={Input_Vat:.2f}')
            if Output_Vat >  Input_Vat:
                print (f'Vat Payable to government ={Output_Vat - Input_Vat:.2f}')
            elif Output_Vat ==  Input_Vat:
                 print ('No VAT payable or receivable ')
            else:
                 print(f'Vat Receivable from government ={ Input_Vat - Output_Vat:.2f}')
