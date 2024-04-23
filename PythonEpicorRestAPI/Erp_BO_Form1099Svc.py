import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.Form1099Svc
# Description: 
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Form1099s(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Form1099s items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Form1099s
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Form1099Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s",headers=creds) as resp:
           return await resp.json()

async def post_Form1099s(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Form1099s
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.Form1099Row
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.Form1099Row
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Form1099s_Company_FormTypeID_Form1099Num(Company, FormTypeID, Form1099Num, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Form1099 item
   Description: Calls GetByID to retrieve the Form1099 item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Form1099
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param Form1099Num: Desc: Form1099Num   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.Form1099Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Form1099s_Company_FormTypeID_Form1099Num(Company, FormTypeID, Form1099Num, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Form1099 for the service
   Description: Calls UpdateExt to update Form1099. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Form1099
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param Form1099Num: Desc: Form1099Num   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.Form1099Row
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Form1099s_Company_FormTypeID_Form1099Num(Company, FormTypeID, Form1099Num, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Form1099 item
   Description: Call UpdateExt to delete Form1099 item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Form1099
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param Form1099Num: Desc: Form1099Num   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")",headers=creds) as resp:
           return await resp.json()

async def get_Form1099s_Company_FormTypeID_Form1099Num_Form1099Dtls(Company, FormTypeID, Form1099Num, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get Form1099Dtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Form1099Dtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param Form1099Num: Desc: Form1099Num   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Form1099DtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")/Form1099Dtls",headers=creds) as resp:
           return await resp.json()

async def get_Form1099s_Company_FormTypeID_Form1099Num_Form1099Dtls_Company_FormTypeID_Form1099Num_Code1099ID(Company, FormTypeID, Form1099Num, Code1099ID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Form1099Dtl item
   Description: Calls GetByID to retrieve the Form1099Dtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Form1099Dtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param Form1099Num: Desc: Form1099Num   Required: True
      :param Code1099ID: Desc: Code1099ID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099s(" + Company + "," + FormTypeID + "," + Form1099Num + ")/Form1099Dtls(" + Company + "," + FormTypeID + "," + Form1099Num + "," + Code1099ID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Form1099Dtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Form1099Dtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Form1099Dtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Form1099DtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls",headers=creds) as resp:
           return await resp.json()

async def post_Form1099Dtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Form1099Dtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Form1099Dtls_Company_FormTypeID_Form1099Num_Code1099ID(Company, FormTypeID, Form1099Num, Code1099ID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Form1099Dtl item
   Description: Calls GetByID to retrieve the Form1099Dtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Form1099Dtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param Form1099Num: Desc: Form1099Num   Required: True
      :param Code1099ID: Desc: Code1099ID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls(" + Company + "," + FormTypeID + "," + Form1099Num + "," + Code1099ID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Form1099Dtls_Company_FormTypeID_Form1099Num_Code1099ID(Company, FormTypeID, Form1099Num, Code1099ID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Form1099Dtl for the service
   Description: Calls UpdateExt to update Form1099Dtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Form1099Dtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param Form1099Num: Desc: Form1099Num   Required: True
      :param Code1099ID: Desc: Code1099ID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.Form1099DtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls(" + Company + "," + FormTypeID + "," + Form1099Num + "," + Code1099ID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Form1099Dtls_Company_FormTypeID_Form1099Num_Code1099ID(Company, FormTypeID, Form1099Num, Code1099ID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Form1099Dtl item
   Description: Call UpdateExt to delete Form1099Dtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Form1099Dtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param Form1099Num: Desc: Form1099Num   Required: True
      :param Code1099ID: Desc: Code1099ID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/Form1099Dtls(" + Company + "," + FormTypeID + "," + Form1099Num + "," + Code1099ID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Form1099ListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseForm1099, whereClauseForm1099Dtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseForm1099=" + whereClauseForm1099
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseForm1099Dtl=" + whereClauseForm1099Dtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(formTypeID, form1099Num, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "formTypeID=" + formTypeID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "form1099Num=" + form1099Num

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChange1099Code(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChange1099Code
   Description: Call this method when the user enters the Form1099Dtl.Code1099ID
   OperationID: OnChange1099Code
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChange1099Code_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChange1099Code_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBoxAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBoxAmount
   Description: Call this method when the user enters the Form1099Dtl.BoxAmt
   OperationID: OnChangeBoxAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBoxAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBoxAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBoxNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBoxNum
   Description: Call this method when the user enters the ttForm1099Dtl.BoxNum
   OperationID: OnChangeBoxNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBoxNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBoxNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendor
   Description: Call this method when the user enters the ttForm1099.VendorID
   OperationID: OnChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Void1099Form(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Void1099Form
   Description: Void 1099 Form by Action Menu from UI
   OperationID: Void1099Form
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Void1099Form_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Void1099Form_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUpdate
   Description: Validate the record was updated
   OperationID: ValidateUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultFormType(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultFormType
   Description: Obtain Default value for 1099 Form Type combo
   OperationID: GetDefaultFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateFormTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFormTypeID
   Description: Returns a description of the entered 1099 Form Type
   OperationID: ValidateFormTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFormTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFormTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckFormTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckFormTypeID
   Description: Checks 1099 Form Type entered
   OperationID: CheckFormTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFormTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFormTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDSite
   OperationID: GetByIDSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewForm1099(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewForm1099
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewForm1099
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewForm1099_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForm1099_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewForm1099Dtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewForm1099Dtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewForm1099Dtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewForm1099Dtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForm1099Dtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Form1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099DtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_Form1099DtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099ListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_Form1099ListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Form1099Row:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_Form1099Row] = obj["value"]
      pass

class Erp_Tablesets_Form1099DtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.Form1099Num:int = obj["Form1099Num"]
      """  1099 Form Number  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.BoxAmt:int = obj["BoxAmt"]
      """  Box Amount  """  
      self.BoxNum:str = obj["BoxNum"]
      """  Box Number  """  
      self.BoxNumDesc:str = obj["BoxNumDesc"]
      """  Box Number Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_Form1099ListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.Form1099Num:int = obj["Form1099Num"]
      """  1099 Form Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_Form1099Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.Form1099Num:int = obj["Form1099Num"]
      """  1099 Form Number  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.Address1:str = obj["Address1"]
      """  First address line of the Supplier Address  """  
      self.Address2:str = obj["Address2"]
      """  Second address line of the Supplier Address  """  
      self.Address3:str = obj["Address3"]
      """  Third address line of the Supplier Address  """  
      self.City:str = obj["City"]
      """  Supplier City  """  
      self.State:str = obj["State"]
      """  Supplier State  """  
      self.ZIP:str = obj["ZIP"]
      """  Supplier Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  County Number for Non US Suppliers  """  
      self.Country:str = obj["Country"]
      """  Country Name  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  Second TIN Notice  """  
      self.Corrected:bool = obj["Corrected"]
      """  Corrected  """  
      self.TwoStepCorrection:bool = obj["TwoStepCorrection"]
      """  2 Step Correction  """  
      self.UserModified:bool = obj["UserModified"]
      """  User Modified  """  
      self.Void:bool = obj["Void"]
      """  Void  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.Submitted:bool = obj["Submitted"]
      """  Submitted  """  
      self.SubmittedElectronic:bool = obj["SubmittedElectronic"]
      """  Indicates that the form was submitted  electronically  """  
      self.ElectronicDate:str = obj["ElectronicDate"]
      """  Date submitted electronically  """  
      self.PaymentYear:int = obj["PaymentYear"]
      """  Payment Year  """  
      self.TINType:str = obj["TINType"]
      """  TIN Type. Values are 1 for EIN, 2 for SSNs, ITINs, and ATINs and 0 if type of TIN is not terminable.  """  
      self.CorrectionOf:int = obj["CorrectionOf"]
      """  Correction of, it is an existing 1099 Form Number which was already generated for selected year/supplier or TIN/TYPE.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.CorrectedBy:int = obj["CorrectedBy"]
      """  Corrected By  """  
      self.Name1:str = obj["Name1"]
      """  First line of the Supplier Name  """  
      self.Name2:str = obj["Name2"]
      """  Second line of the Supplier Name  """  
      self.NameControl:str = obj["NameControl"]
      """  Name Control, optional and used for electronic export  """  
      self.AccountNum:str = obj["AccountNum"]
      """  Payee Account Number  """  
      self.TIN:str = obj["TIN"]
      """  Supplier TIN  """  
      self.TimeSubmitted:int = obj["TimeSubmitted"]
      """  Ttime submitted electronically  """  
      self.GenDate:str = obj["GenDate"]
      """  Generation Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NonUS:bool = obj["NonUS"]
      """  Non US Supplier  """  
      self.FATCA:bool = obj["FATCA"]
      """  FATCA  """  
      self.US1099KTranType:str = obj["US1099KTranType"]
      """  Form 1099-K Transaction Type  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  Form 1099-K Merchant Category Code  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.CompanyAddress:str = obj["CompanyAddress"]
      """  Company Address  """  
      self.CompanyAddress2:str = obj["CompanyAddress2"]
      """  Company Address 2nd Line  """  
      self.CompanyAddress3:str = obj["CompanyAddress3"]
      """  Company Address 3rd Line  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  City portion of company address  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyName2:str = obj["CompanyName2"]
      """  Company Name 2nd Line  """  
      self.CompanyState:str = obj["CompanyState"]
      """  State portion of company address  """  
      self.CompanyTIN:str = obj["CompanyTIN"]
      """  Company TIN  """  
      self.CompanyZIP:str = obj["CompanyZIP"]
      """  Postal code or zip code portion of company address.  """  
      self.CountryPhone:str = obj["CountryPhone"]
      """  Company phone number  """  
      self.ModifiedAndSaved:bool = obj["ModifiedAndSaved"]
      """  Check field to determine wheter the record was modified by the user or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.VendorVendorNum:int = obj["VendorVendorNum"]
      self.VendorNonUS:bool = obj["VendorNonUS"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorAccountNum:str = obj["VendorAccountNum"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorNameControl:str = obj["VendorNameControl"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorReporting1099Name:str = obj["VendorReporting1099Name"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCountryNum:int = obj["VendorCountryNum"]
      self.VendorFATCA:bool = obj["VendorFATCA"]
      self.VendorReporting1099Name2:str = obj["VendorReporting1099Name2"]
      self.VendorSecondTINNotice:bool = obj["VendorSecondTINNotice"]
      self.VendorTINType:str = obj["VendorTINType"]
      self.VendorTIN:str = obj["VendorTIN"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckFormTypeID_input:
   """ Required : 
   newFormTypeID
   """  
   def __init__(self, obj):
      self.newFormTypeID:str = obj["newFormTypeID"]
      pass

class CheckFormTypeID_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   formTypeID
   form1099Num
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      self.form1099Num:int = obj["form1099Num"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_Form1099DtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.Form1099Num:int = obj["Form1099Num"]
      """  1099 Form Number  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.BoxAmt:int = obj["BoxAmt"]
      """  Box Amount  """  
      self.BoxNum:str = obj["BoxNum"]
      """  Box Number  """  
      self.BoxNumDesc:str = obj["BoxNumDesc"]
      """  Box Number Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_Form1099ListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.Form1099Num:int = obj["Form1099Num"]
      """  1099 Form Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_Form1099ListTableset:
   def __init__(self, obj):
      self.Form1099List:list[Erp_Tablesets_Form1099ListRow] = obj["Form1099List"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_Form1099Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.Form1099Num:int = obj["Form1099Num"]
      """  1099 Form Number  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.Address1:str = obj["Address1"]
      """  First address line of the Supplier Address  """  
      self.Address2:str = obj["Address2"]
      """  Second address line of the Supplier Address  """  
      self.Address3:str = obj["Address3"]
      """  Third address line of the Supplier Address  """  
      self.City:str = obj["City"]
      """  Supplier City  """  
      self.State:str = obj["State"]
      """  Supplier State  """  
      self.ZIP:str = obj["ZIP"]
      """  Supplier Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  County Number for Non US Suppliers  """  
      self.Country:str = obj["Country"]
      """  Country Name  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  Second TIN Notice  """  
      self.Corrected:bool = obj["Corrected"]
      """  Corrected  """  
      self.TwoStepCorrection:bool = obj["TwoStepCorrection"]
      """  2 Step Correction  """  
      self.UserModified:bool = obj["UserModified"]
      """  User Modified  """  
      self.Void:bool = obj["Void"]
      """  Void  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.Submitted:bool = obj["Submitted"]
      """  Submitted  """  
      self.SubmittedElectronic:bool = obj["SubmittedElectronic"]
      """  Indicates that the form was submitted  electronically  """  
      self.ElectronicDate:str = obj["ElectronicDate"]
      """  Date submitted electronically  """  
      self.PaymentYear:int = obj["PaymentYear"]
      """  Payment Year  """  
      self.TINType:str = obj["TINType"]
      """  TIN Type. Values are 1 for EIN, 2 for SSNs, ITINs, and ATINs and 0 if type of TIN is not terminable.  """  
      self.CorrectionOf:int = obj["CorrectionOf"]
      """  Correction of, it is an existing 1099 Form Number which was already generated for selected year/supplier or TIN/TYPE.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.CorrectedBy:int = obj["CorrectedBy"]
      """  Corrected By  """  
      self.Name1:str = obj["Name1"]
      """  First line of the Supplier Name  """  
      self.Name2:str = obj["Name2"]
      """  Second line of the Supplier Name  """  
      self.NameControl:str = obj["NameControl"]
      """  Name Control, optional and used for electronic export  """  
      self.AccountNum:str = obj["AccountNum"]
      """  Payee Account Number  """  
      self.TIN:str = obj["TIN"]
      """  Supplier TIN  """  
      self.TimeSubmitted:int = obj["TimeSubmitted"]
      """  Ttime submitted electronically  """  
      self.GenDate:str = obj["GenDate"]
      """  Generation Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NonUS:bool = obj["NonUS"]
      """  Non US Supplier  """  
      self.FATCA:bool = obj["FATCA"]
      """  FATCA  """  
      self.US1099KTranType:str = obj["US1099KTranType"]
      """  Form 1099-K Transaction Type  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  Form 1099-K Merchant Category Code  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.CompanyAddress:str = obj["CompanyAddress"]
      """  Company Address  """  
      self.CompanyAddress2:str = obj["CompanyAddress2"]
      """  Company Address 2nd Line  """  
      self.CompanyAddress3:str = obj["CompanyAddress3"]
      """  Company Address 3rd Line  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  City portion of company address  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyName2:str = obj["CompanyName2"]
      """  Company Name 2nd Line  """  
      self.CompanyState:str = obj["CompanyState"]
      """  State portion of company address  """  
      self.CompanyTIN:str = obj["CompanyTIN"]
      """  Company TIN  """  
      self.CompanyZIP:str = obj["CompanyZIP"]
      """  Postal code or zip code portion of company address.  """  
      self.CountryPhone:str = obj["CountryPhone"]
      """  Company phone number  """  
      self.ModifiedAndSaved:bool = obj["ModifiedAndSaved"]
      """  Check field to determine wheter the record was modified by the user or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.VendorVendorNum:int = obj["VendorVendorNum"]
      self.VendorNonUS:bool = obj["VendorNonUS"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorAccountNum:str = obj["VendorAccountNum"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorNameControl:str = obj["VendorNameControl"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorReporting1099Name:str = obj["VendorReporting1099Name"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCountryNum:int = obj["VendorCountryNum"]
      self.VendorFATCA:bool = obj["VendorFATCA"]
      self.VendorReporting1099Name2:str = obj["VendorReporting1099Name2"]
      self.VendorSecondTINNotice:bool = obj["VendorSecondTINNotice"]
      self.VendorTINType:str = obj["VendorTINType"]
      self.VendorTIN:str = obj["VendorTIN"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_Form1099Tableset:
   def __init__(self, obj):
      self.Form1099:list[Erp_Tablesets_Form1099Row] = obj["Form1099"]
      self.Form1099Dtl:list[Erp_Tablesets_Form1099DtlRow] = obj["Form1099Dtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtForm1099Tableset:
   def __init__(self, obj):
      self.Form1099:list[Erp_Tablesets_Form1099Row] = obj["Form1099"]
      self.Form1099Dtl:list[Erp_Tablesets_Form1099DtlRow] = obj["Form1099Dtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDSite_input:
   """ Required : 
   formTypeID
   form1099Num
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      """  1099 Form Type  """  
      self.form1099Num:int = obj["form1099Num"]
      """  1099 Form Number  """  
      pass

class GetByIDSite_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Form1099Tableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   formTypeID
   form1099Num
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      self.form1099Num:int = obj["form1099Num"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Form1099Tableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Form1099Tableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Form1099Tableset] = obj["returnObj"]
      pass

class GetDefaultFormType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultFormType:str = obj["parameters"]
      self.defaultFormTypeDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Form1099ListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewForm1099Dtl_input:
   """ Required : 
   ds
   formTypeID
   form1099Num
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      self.formTypeID:str = obj["formTypeID"]
      self.form1099Num:int = obj["form1099Num"]
      pass

class GetNewForm1099Dtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewForm1099_input:
   """ Required : 
   ds
   formTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      self.formTypeID:str = obj["formTypeID"]
      pass

class GetNewForm1099_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseForm1099
   whereClauseForm1099Dtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseForm1099:str = obj["whereClauseForm1099"]
      self.whereClauseForm1099Dtl:str = obj["whereClauseForm1099Dtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Form1099Tableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class OnChange1099Code_input:
   """ Required : 
   formTypeID
   p1099Code
   ds
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      """  Form Type - Code for Form Type  """  
      self.p1099Code:str = obj["p1099Code"]
      """  1099 Code - 1099 Code  """  
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

class OnChange1099Code_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBoxAmount_input:
   """ Required : 
   formTypeID
   p1099Code
   boxAmount
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      """  Form Type - Code for Form Type  """  
      self.p1099Code:str = obj["p1099Code"]
      """  1099 Code - 1099 Code  """  
      self.boxAmount:int = obj["boxAmount"]
      """  Box Amount - Amount for the box line  """  
      pass

class OnChangeBoxAmount_output:
   def __init__(self, obj):
      pass

class OnChangeBoxNum_input:
   """ Required : 
   formTypeID
   boxNum
   ds
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      """  Form Type - Code for Form Type  """  
      self.boxNum:str = obj["boxNum"]
      """  Box Number - Code for Box Number  """  
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

class OnChangeBoxNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendor_input:
   """ Required : 
   vendorId
   ds
   """  
   def __init__(self, obj):
      self.vendorId:str = obj["vendorId"]
      """  Vendor ID  """  
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

class OnChangeVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtForm1099Tableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtForm1099Tableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateFormTypeID_input:
   """ Required : 
   formTypeID
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      pass

class ValidateFormTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.formTypeIDDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateUpdate_input:
   """ Required : 
   formTypeID
   form1099Num
   ds
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      """  Form Type - Code for Form Type  """  
      self.form1099Num:int = obj["form1099Num"]
      """  Form Number - 1099 Form Number  """  
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

class ValidateUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcresult:bool = obj["pcresult"]
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class Void1099Form_input:
   """ Required : 
   formTypeID
   form1099Num
   ds
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      """  Form Type - Code for Form Type  """  
      self.form1099Num:int = obj["form1099Num"]
      """  Form Number - 1099 Form Number  """  
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

class Void1099Form_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Form1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

