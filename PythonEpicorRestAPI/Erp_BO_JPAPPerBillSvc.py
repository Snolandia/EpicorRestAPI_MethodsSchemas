import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JPAPPerBillSvc
# Description: Japan Localization - AP Periodic Billing Maintenance
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBills(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JPAPPerBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBills
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBills",headers=creds) as resp:
           return await resp.json()

async def post_JPAPPerBills(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBills
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBills", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBills_Company_VendorNum(Company, VendorNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBill item
   Description: Calls GetByID to retrieve the JPAPPerBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBills(" + Company + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JPAPPerBills_Company_VendorNum(Company, VendorNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JPAPPerBill for the service
   Description: Calls UpdateExt to update JPAPPerBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBills(" + Company + "," + VendorNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JPAPPerBills_Company_VendorNum(Company, VendorNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JPAPPerBill item
   Description: Call UpdateExt to delete JPAPPerBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBills(" + Company + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBills_Company_VendorNum_JPAPPerBillDtls(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get JPAPPerBillDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JPAPPerBillDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBills(" + Company + "," + VendorNum + ")/JPAPPerBillDtls",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBills_Company_VendorNum_JPAPPerBillDtls_Company_VendorNum_SummarizationDay(Company, VendorNum, SummarizationDay, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillDtl item
   Description: Calls GetByID to retrieve the JPAPPerBillDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param SummarizationDay: Desc: SummarizationDay   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBills(" + Company + "," + VendorNum + ")/JPAPPerBillDtls(" + Company + "," + VendorNum + "," + SummarizationDay + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JPAPPerBillDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBillDtls",headers=creds) as resp:
           return await resp.json()

async def post_JPAPPerBillDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBillDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JPAPPerBillDtls_Company_VendorNum_SummarizationDay(Company, VendorNum, SummarizationDay, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPAPPerBillDtl item
   Description: Calls GetByID to retrieve the JPAPPerBillDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param SummarizationDay: Desc: SummarizationDay   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBillDtls(" + Company + "," + VendorNum + "," + SummarizationDay + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JPAPPerBillDtls_Company_VendorNum_SummarizationDay(Company, VendorNum, SummarizationDay, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JPAPPerBillDtl for the service
   Description: Calls UpdateExt to update JPAPPerBillDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param SummarizationDay: Desc: SummarizationDay   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBillDtls(" + Company + "," + VendorNum + "," + SummarizationDay + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JPAPPerBillDtls_Company_VendorNum_SummarizationDay(Company, VendorNum, SummarizationDay, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JPAPPerBillDtl item
   Description: Call UpdateExt to delete JPAPPerBillDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param SummarizationDay: Desc: SummarizationDay   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/JPAPPerBillDtls(" + Company + "," + VendorNum + "," + SummarizationDay + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJPAPPerBillHead, whereClauseJPAPPerBillDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseJPAPPerBillHead=" + whereClauseJPAPPerBillHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJPAPPerBillDtl=" + whereClauseJPAPPerBillDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "vendorNum=" + vendorNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorNumByVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorNumByVendorID
   Description: Returns a Vendor Num given the Vendor ID.
   OperationID: GetVendorNumByVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorNumByVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorNumByVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByVendorID
   Description: Returns a DataSet given the Vendor ID.
   OperationID: GetByVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSummDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSummDay
   Description: Validates that the Summarization Day is unique for given supplier.
   OperationID: ValidateSummDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSummDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSummDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJPAPPerBillHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJPAPPerBillHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJPAPPerBillDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJPAPPerBillDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JPAPPerBillDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JPAPPerBillHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JPAPPerBillHeadRow] = obj["value"]
      pass

class Erp_Tablesets_JPAPPerBillDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.SummarizationDay:int = obj["SummarizationDay"]
      """  SummarizationDay  """  
      self.EndOfMonth:bool = obj["EndOfMonth"]
      """  EndOfMonth  """  
      self.TermsCode:str = obj["TermsCode"]
      """  TermsCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.PerBillStatus:bool = obj["PerBillStatus"]
      """  PerBillStatus  """  
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      """  DueDateCriteria  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.VendLnkVendorID:str = obj["VendLnkVendorID"]
      self.VendLnkName:str = obj["VendLnkName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.PerBillStatus:bool = obj["PerBillStatus"]
      """  PerBillStatus  """  
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      """  DueDateCriteria  """  
      self.DynCalID1:str = obj["DynCalID1"]
      """  DynCalID1  """  
      self.DynCalID2:str = obj["DynCalID2"]
      """  DynCalID2  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.VendLnkVendorID:str = obj["VendLnkVendorID"]
      self.VendLnkName:str = obj["VendLnkName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   vendorNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JPAPPerBillDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.SummarizationDay:int = obj["SummarizationDay"]
      """  SummarizationDay  """  
      self.EndOfMonth:bool = obj["EndOfMonth"]
      """  EndOfMonth  """  
      self.TermsCode:str = obj["TermsCode"]
      """  TermsCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.PerBillStatus:bool = obj["PerBillStatus"]
      """  PerBillStatus  """  
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      """  DueDateCriteria  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.VendLnkVendorID:str = obj["VendLnkVendorID"]
      self.VendLnkName:str = obj["VendLnkName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillHeadListTableset:
   def __init__(self, obj):
      self.JPAPPerBillHeadList:list[Erp_Tablesets_JPAPPerBillHeadListRow] = obj["JPAPPerBillHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JPAPPerBillHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.PerBillStatus:bool = obj["PerBillStatus"]
      """  PerBillStatus  """  
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      """  DueDateCriteria  """  
      self.DynCalID1:str = obj["DynCalID1"]
      """  DynCalID1  """  
      self.DynCalID2:str = obj["DynCalID2"]
      """  DynCalID2  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.VendLnkVendorID:str = obj["VendLnkVendorID"]
      self.VendLnkName:str = obj["VendLnkName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JPAPPerBillTableset:
   def __init__(self, obj):
      self.JPAPPerBillHead:list[Erp_Tablesets_JPAPPerBillHeadRow] = obj["JPAPPerBillHead"]
      self.JPAPPerBillDtl:list[Erp_Tablesets_JPAPPerBillDtlRow] = obj["JPAPPerBillDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtJPAPPerBillTableset:
   def __init__(self, obj):
      self.JPAPPerBillHead:list[Erp_Tablesets_JPAPPerBillHeadRow] = obj["JPAPPerBillHead"]
      self.JPAPPerBillDtl:list[Erp_Tablesets_JPAPPerBillDtlRow] = obj["JPAPPerBillDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPAPPerBillTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPAPPerBillTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPAPPerBillTableset] = obj["returnObj"]
      pass

class GetByVendorID_input:
   """ Required : 
   vendorID
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      pass

class GetByVendorID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPAPPerBillTableset] = obj["returnObj"]
      pass

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
      self.returnObj:list[Erp_Tablesets_JPAPPerBillHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJPAPPerBillDtl_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewJPAPPerBillDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJPAPPerBillHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillTableset] = obj["ds"]
      pass

class GetNewJPAPPerBillHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJPAPPerBillHead
   whereClauseJPAPPerBillDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJPAPPerBillHead:str = obj["whereClauseJPAPPerBillHead"]
      self.whereClauseJPAPPerBillDtl:str = obj["whereClauseJPAPPerBillDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPAPPerBillTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVendorNumByVendorID_input:
   """ Required : 
   vendorID
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      pass

class GetVendorNumByVendorID_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJPAPPerBillTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJPAPPerBillTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPAPPerBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSummDay_input:
   """ Required : 
   vendorNum
   summDay
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.summDay:int = obj["summDay"]
      pass

class ValidateSummDay_output:
   def __init__(self, obj):
      pass

