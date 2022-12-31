#!/bin/bash
#script to insert data from data4_models.csv into database fu_expenses

PSQL="docker exec db-postgresql psql --username=orfeo --dbname=fu_expenses -t --no-align -c"
echo $($PSQL 'TRUNCATE ""FU_expenses_App_monthly_check", FU_expenses_App_category", "FU_expenses_App_payment_method", "FU_expenses_App_entity", "FU_expenses_App_bank_product" ')
cat data4_models.csv | while IFS="," read CATEGORY METHOD ENTITY PRODUCT
do
    if [[ $CATEGORY != Category ]]
    then 
        # valida if the category already exists
        CATE=$($PSQL 'SELECT name FROM "FU_expenses_App_category" WHERE category_name = '$CATEGORY' ')
        if [[ -z $CATE ]]
        then
            #insert category in category table 
            INSERT_CATEGORY=$($PSQL 'INSERT INTO "FU_expenses_App_category"(category_name) VALUES('$CATEGORY')')
            if [[ $INSERT_CATEGORY == 'INSERT 0 1' ]]
            then 
                echo Inserted into category
            fi
        fi
    fi
done



    

