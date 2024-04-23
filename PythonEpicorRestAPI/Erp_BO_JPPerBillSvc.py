import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JPPerBillSvc
# Description: Japan Localization - Periodic Billing Maintenance
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JPPerBills(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JPPerBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPPerBills
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/JPPerBills",headers=creds) as resp:
           return await resp.json()

async def post_JPPerBills(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPPerBills
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerBillHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/JPPerBills", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JPPerBills_Company_CustNum(Company, CustNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JPPerBill item
   Description: Calls GetByID to retrieve the JPPerBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPPerBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/JPPerBills(" + Company + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JPPerBills_Company_CustNum(Company, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JPPerBill for the service
   Description: Calls UpdateExt to update JPPerBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPPerBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/JPPerBills(" + Company + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JPPerBills_Company_CustNum(Company, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JPPerBill item
   Description: Call UpdateExt to delete JPPerBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPPerBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/JPPerBills(" + Company + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_JPPerBills_Company_CustNum_PerBillDtls(Company, CustNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PerBillDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerBillDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/JPPerBills(" + Company + "," + CustNum + ")/PerBillDtls",headers=creds) as resp:
           return await resp.json()

async def get_JPPerBills_Company_CustNum_PerBillDtls_Company_CustNum_SummarizationDay_EndOfMonth(Company, CustNum, SummarizationDay, EndOfMonth, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerBillDtl item
   Description: Calls GetByID to retrieve the PerBillDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param SummarizationDay: Desc: SummarizationDay   Required: True
      :param EndOfMonth: Desc: EndOfMonth   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/JPPerBills(" + Company + "," + CustNum + ")/PerBillDtls(" + Company + "," + CustNum + "," + SummarizationDay + "," + EndOfMonth + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerBillDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PerBillDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerBillDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/PerBillDtls",headers=creds) as resp:
           return await resp.json()

async def post_PerBillDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerBillDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerBillDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/PerBillDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PerBillDtls_Company_CustNum_SummarizationDay_EndOfMonth(Company, CustNum, SummarizationDay, EndOfMonth, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerBillDtl item
   Description: Calls GetByID to retrieve the PerBillDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param SummarizationDay: Desc: SummarizationDay   Required: True
      :param EndOfMonth: Desc: EndOfMonth   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerBillDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/PerBillDtls(" + Company + "," + CustNum + "," + SummarizationDay + "," + EndOfMonth + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PerBillDtls_Company_CustNum_SummarizationDay_EndOfMonth(Company, CustNum, SummarizationDay, EndOfMonth, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PerBillDtl for the service
   Description: Calls UpdateExt to update PerBillDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerBillDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param SummarizationDay: Desc: SummarizationDay   Required: True
      :param EndOfMonth: Desc: EndOfMonth   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/PerBillDtls(" + Company + "," + CustNum + "," + SummarizationDay + "," + EndOfMonth + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PerBillDtls_Company_CustNum_SummarizationDay_EndOfMonth(Company, CustNum, SummarizationDay, EndOfMonth, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PerBillDtl item
   Description: Call UpdateExt to delete PerBillDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerBillDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param SummarizationDay: Desc: SummarizationDay   Required: True
      :param EndOfMonth: Desc: EndOfMonth   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/PerBillDtls(" + Company + "," + CustNum + "," + SummarizationDay + "," + EndOfMonth + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePerBillHead, whereClausePerBillDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePerBillHead=" + whereClausePerBillHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerBillDtl=" + whereClausePerBillDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(custNum, epicorHeaders = None):
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
   params += "custNum=" + custNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCustNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustNum
   Description: Receives CustId, returns CustNum
   OperationID: GetCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByCustID
   Description: Returns a DataSet given the Customer ID.
   OperationID: GetByCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSummDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSummDay
   Description: Validates that the Summarization Day is unique.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerBillHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerBillHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerBillHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerBillDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerBillDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerBillDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerBillDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerBillHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerBillHeadRow] = obj["value"]
      pass

class Erp_Tablesets_PerBillDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.SummarizationDay:int = obj["SummarizationDay"]
      """  Summarization Day. A  day when a company sums up accounts receivables for each customer. Used to calculate Billing Period and Date.  """  
      self.EndOfMonth:bool = obj["EndOfMonth"]
      """  End of Month  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  A periodic between the billing or summarizing date and the due date.  """  
      self.TermsDescription:str = obj["TermsDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.PerBillStatus:bool = obj["PerBillStatus"]
      """  Periodic Billing Status  """  
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      """  Criteria used for the calculation of the due date. Only enable if Periodic Billing status is active.  """  
      self.PerBillTerms:int = obj["PerBillTerms"]
      """  Periodic Billing Terms. A period between the billing or summarizing date and the due date (for example: 30 days, 45 days, 60 days).  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.PerBillStatus:bool = obj["PerBillStatus"]
      """  Periodic Billing Status  """  
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      """  Criteria used for the calculation of the due date. Only enable if Periodic Billing status is active.  """  
      self.PerBillTerms:int = obj["PerBillTerms"]
      """  Periodic Billing Terms. A period between the billing or summarizing date and the due date (for example: 30 days, 45 days, 60 days).  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DynCalID1:str = obj["DynCalID1"]
      """  Dynamic Calendar to hold/configurate holiday and negotiated days that will be shifted backward or forward one day.  """  
      self.DynCalID2:str = obj["DynCalID2"]
      """  Dynamic Calendar to hold/configurate holiday and negotiated days that will be shifted backward or forward one day  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   custNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JPPerBillTableset:
   def __init__(self, obj):
      self.PerBillHead:list[Erp_Tablesets_PerBillHeadRow] = obj["PerBillHead"]
      self.PerBillDtl:list[Erp_Tablesets_PerBillDtlRow] = obj["PerBillDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PerBillDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.SummarizationDay:int = obj["SummarizationDay"]
      """  Summarization Day. A  day when a company sums up accounts receivables for each customer. Used to calculate Billing Period and Date.  """  
      self.EndOfMonth:bool = obj["EndOfMonth"]
      """  End of Month  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  A periodic between the billing or summarizing date and the due date.  """  
      self.TermsDescription:str = obj["TermsDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.PerBillStatus:bool = obj["PerBillStatus"]
      """  Periodic Billing Status  """  
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      """  Criteria used for the calculation of the due date. Only enable if Periodic Billing status is active.  """  
      self.PerBillTerms:int = obj["PerBillTerms"]
      """  Periodic Billing Terms. A period between the billing or summarizing date and the due date (for example: 30 days, 45 days, 60 days).  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerBillHeadListTableset:
   def __init__(self, obj):
      self.PerBillHeadList:list[Erp_Tablesets_PerBillHeadListRow] = obj["PerBillHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PerBillHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.PerBillStatus:bool = obj["PerBillStatus"]
      """  Periodic Billing Status  """  
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      """  Criteria used for the calculation of the due date. Only enable if Periodic Billing status is active.  """  
      self.PerBillTerms:int = obj["PerBillTerms"]
      """  Periodic Billing Terms. A period between the billing or summarizing date and the due date (for example: 30 days, 45 days, 60 days).  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DynCalID1:str = obj["DynCalID1"]
      """  Dynamic Calendar to hold/configurate holiday and negotiated days that will be shifted backward or forward one day.  """  
      self.DynCalID2:str = obj["DynCalID2"]
      """  Dynamic Calendar to hold/configurate holiday and negotiated days that will be shifted backward or forward one day  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtJPPerBillTableset:
   def __init__(self, obj):
      self.PerBillHead:list[Erp_Tablesets_PerBillHeadRow] = obj["PerBillHead"]
      self.PerBillDtl:list[Erp_Tablesets_PerBillDtlRow] = obj["PerBillDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByCustID_input:
   """ Required : 
   custID
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      pass

class GetByCustID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPPerBillTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   custNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPPerBillTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPPerBillTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JPPerBillTableset] = obj["returnObj"]
      pass

class GetCustNum_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  Customer ID  """  
      pass

class GetCustNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCustNum:int = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_PerBillHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPerBillDtl_input:
   """ Required : 
   ds
   custNum
   summarizationDay
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      self.summarizationDay:int = obj["summarizationDay"]
      pass

class GetNewPerBillDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPerBillHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillTableset] = obj["ds"]
      pass

class GetNewPerBillHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePerBillHead
   whereClausePerBillDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePerBillHead:str = obj["whereClausePerBillHead"]
      self.whereClausePerBillDtl:str = obj["whereClausePerBillDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JPPerBillTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJPPerBillTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJPPerBillTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSummDay_input:
   """ Required : 
   ipSummDay
   ds
   """  
   def __init__(self, obj):
      self.ipSummDay:int = obj["ipSummDay"]
      """  Proposed Summarization Day value  """  
      self.ds:list[Erp_Tablesets_JPPerBillTableset] = obj["ds"]
      pass

class ValidateSummDay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JPPerBillTableset] = obj["ds"]
      pass

      """  output parameters  """  

