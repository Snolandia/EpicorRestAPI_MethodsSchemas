import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CashGrpSvc
# Description: bo/CashGrp/CashGrp.p
           Cash Group Entry - separated from CashRec.p
           Jennifer Johnson
           03/18/04
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CashGrps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashGrps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps",headers=creds) as resp:
           return await resp.json()

async def post_CashGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashGrps_Company_GroupID(Company, GroupID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashGrp item
   Description: Calls GetByID to retrieve the CashGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashGrps_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashGrp for the service
   Description: Calls UpdateExt to update CashGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashGrps_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashGrp item
   Description: Call UpdateExt to delete CashGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCashGrp, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseCashGrp=" + whereClauseCashGrp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: This method returns a code/description list string for the table name and field name passed in
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BeforeGetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BeforeGetByID
   Description: This method checks to see if the selected group is in use before fetching the dataset
if the group is in use, the user must answer yes to continue before the GetByID method is run
   OperationID: BeforeGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BeforeGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BeforeGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDNoLock
   Description: Returns a DataSet given the primary key. Active user locking disabled.
   OperationID: GetByIDNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashGrpNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashGrpNoLock
   Description: Inserts a new row in the DataSet with defaults populated. Active user locking disabled.
   OperationID: GetNewCashGrpNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsNoLock
   Description: GetRows method with disabled ActiveUser functionality.
   OperationID: GetRowsNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteZeroAmtTaxRec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteZeroAmtTaxRec
   Description: This method deletes TaxDtl records which have zero amounts
Since Payments TAx logic calculates tax conditionally only for the first tax line the payment could have multiple zero tax records.
   OperationID: DeleteZeroAmtTaxRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteZeroAmtTaxRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZeroAmtTaxRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGrpBankInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGrpBankInfo
   Description: This method is called when the Bank Account changes
   OperationID: GetGrpBankInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGrpBankInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGrpBankInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGrpFiscal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGrpFiscal
   Description: This method is run when the Transaction date is changed to update the fiscal period fields
   OperationID: GetGrpFiscal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGrpFiscal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGrpFiscal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashGrpForPINoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashGrpForPINoLock
   Description: GetNewCashGrpForPI with active user locking disabled.
   OperationID: GetNewCashGrpForPINoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpForPINoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpForPINoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashGrpForPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashGrpForPI
   OperationID: GetNewCashGrpForPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashGrpForPIStatusNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashGrpForPIStatusNoLock
   Description: GetNewCashGrpForPIStatus with active user locking disabled.
   OperationID: GetNewCashGrpForPIStatusNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpForPIStatusNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpForPIStatusNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashGrpForPIStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashGrpForPIStatus
   OperationID: GetNewCashGrpForPIStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpForPIStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpForPIStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPIGroupByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPIGroupByID
   OperationID: GetPIGroupByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPIGroupByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPIGroupByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsPIGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsPIGroup
   Description: This method verifies a Cash Group exists and returns the different types of group flags for further use.
   OperationID: IsPIGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsPIGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPIGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockPIGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockPIGroup
   Description: Should be call before GetPIGroupByID to lock the Group.
   OperationID: LockPIGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockPIGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockPIGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockPIGroupInDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockPIGroupInDS
   Description: Should be call before GetPIGroupByID to lock the Group.
   OperationID: LockPIGroupInDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockPIGroupInDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockPIGroupInDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockPIGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockPIGroup
   Description: Unlock the group.  Only user who locked the group can unlock it.
   OperationID: UnlockPIGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockPIGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockPIGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockPIGroupInDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockPIGroupInDS
   Description: Unlock the group.  Only user who locked the group can unlock it.
   OperationID: UnlockPIGroupInDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockPIGroupInDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockPIGroupInDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPIStatusGroupByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPIStatusGroupByID
   OperationID: GetPIStatusGroupByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPIStatusGroupByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPIStatusGroupByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveCashGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveCashGrp
   Description: This method must be run whenever the use is leaving the current CashGrp record
(either by selecting a new Group or by leaving the screen)
   OperationID: LeaveCashGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveCashGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveCashGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostEPGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostEPGroup
   Description: This method is for Electronically processed group
This method first checks if the Group Receipt/Payment was processed and CashGrp.EIPaymSent field is true
This method checks that the A/R is interfaced to the G/L. If not, then ask the
user if they want to go ahead and post the cash receipts
   OperationID: PrePostEPGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostEPGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostEPGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostGroup
   Description: This method checks that the A/R is interfaced to the G/L.  If not, then ask the
user if they want to go ahead and post the cash receipts
This method also checks if this Group has any related Tax Records with 0 amounts
The user is asked if these records are supposed to be deleted before Post
   OperationID: PrePostGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMaster
   Description: This method is called instead of the standard Update
   OperationID: UpdateMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiptGroupExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiptGroupExists
   Description: This method is called to check if group with entered ID exists
   OperationID: ReceiptGroupExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiptGroupExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiptGroupExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListDepositSlips(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListDepositSlips
   Description: Returns a List Dataset for DepositSlips
   OperationID: GetListDepositSlips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListDepositSlips_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListDepositSlips_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsUseLockSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsUseLockSetting
   Description: Returns the CashGrp dataset using the Auto Lock Group functionality
   OperationID: GetRowsUseLockSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsUseLockSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsUseLockSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GroupUnlock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GroupUnlock
   Description: Clears the lock of a group, only if the user of the current session is the same as the one locking the group.
This method update the database and refresh the group dataset with the information from the database.
Returns the dataset with the current lock status of GLJrnGrp.
   OperationID: GroupUnlock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupUnlock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupUnlock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GroupLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GroupLock
   Description: Locks the groupID for the current user in session only if the group is not locked already
This method update the database and refresh the group dataset with the information from the database.
Returns the dataset with the current lock status of GLJrnGrp.
   OperationID: GroupLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashGrpRow] = obj["value"]
      pass

class Erp_Tablesets_CashGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this. This value is then duplicated into the CashHead and CashDtl as part of the Post process. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period. This is then duplicated into the CashHead and CashDtl during posting process.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Related record to a  BankAcct.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  If yes, indicates that the group is for Payment Instrument.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  Flag indicating payments were processed  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Payment Instrument Status  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  Indicates its a PI Status Change group  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalApplied:int = obj["TotalApplied"]
      self.UnappliedBalance:int = obj["UnappliedBalance"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.TotalDeposit:int = obj["TotalDeposit"]
      self.TotalMisc:int = obj["TotalMisc"]
      self.TotalARAmount:int = obj["TotalARAmount"]
      self.TotalWithhold:int = obj["TotalWithhold"]
      self.PostErrorLog:str = obj["PostErrorLog"]
      self.PostToGL:bool = obj["PostToGL"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BankCurrencyCodeDocumentDesc:str = obj["BankCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BankCurrencyCodeCurrencyID:str = obj["BankCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BankCurrencyCodeCurrName:str = obj["BankCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BankCurrencyCodeCurrDesc:str = obj["BankCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.BankCurrencyCodeCurrSymbol:str = obj["BankCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.PMType:int = obj["PMType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.PMName:str = obj["PMName"]
      """  Name of the payment method  """  
      self.PMSummarizePerCustomer:bool = obj["PMSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.TotalWriteOff:int = obj["TotalWriteOff"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this. This value is then duplicated into the CashHead and CashDtl as part of the Post process. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period. This is then duplicated into the CashHead and CashDtl during posting process.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Related record to a  BankAcct.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  If yes, indicates that the group is for Payment Instrument.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  Flag indicating payments were processed  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Payment Instrument Status  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  Indicates its a PI Status Change group  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Auto Generated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.BankCurrencyCodeCurrDesc:str = obj["BankCurrencyCodeCurrDesc"]
      self.BankCurrencyCodeCurrencyID:str = obj["BankCurrencyCodeCurrencyID"]
      self.BankCurrencyCodeCurrName:str = obj["BankCurrencyCodeCurrName"]
      self.BankCurrencyCodeCurrSymbol:str = obj["BankCurrencyCodeCurrSymbol"]
      self.BankCurrencyCodeDocumentDesc:str = obj["BankCurrencyCodeDocumentDesc"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DepSlipGrouping:bool = obj["DepSlipGrouping"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      self.EIGrouping:bool = obj["EIGrouping"]
      self.PostErrorLog:str = obj["PostErrorLog"]
      self.PostToGL:bool = obj["PostToGL"]
      self.TotalApplied:int = obj["TotalApplied"]
      self.TotalARAmount:int = obj["TotalARAmount"]
      self.TotalBankFee:int = obj["TotalBankFee"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalDeposit:int = obj["TotalDeposit"]
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.TotalMisc:int = obj["TotalMisc"]
      self.TotalWithhold:int = obj["TotalWithhold"]
      self.UIGrouping:bool = obj["UIGrouping"]
      self.UnappliedBalance:int = obj["UnappliedBalance"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.TotalWriteOff:int = obj["TotalWriteOff"]
      self.IsDocumentLocked:bool = obj["IsDocumentLocked"]
      """  Shows that the group contains payments which are in review  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: a payment is already in review journal or in posting process.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.PIStatusPIStage:str = obj["PIStatusPIStage"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PMARIDTiming:int = obj["PMARIDTiming"]
      self.PMName:str = obj["PMName"]
      self.PMType:int = obj["PMType"]
      self.PMSummarizePerCustomer:bool = obj["PMSummarizePerCustomer"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BeforeGetByID_input:
   """ Required : 
   groupID
   ipCheckUserID
   ipNeedQuestion
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Selected Group ID  """  
      self.ipCheckUserID:bool = obj["ipCheckUserID"]
      """  Check group is in use  """  
      self.ipNeedQuestion:bool = obj["ipNeedQuestion"]
      """  If false, only warning about the group is in use  """  
      pass

class BeforeGetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.vQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteZeroAmtTaxRec_input:
   """ Required : 
   postGroupID
   """  
   def __init__(self, obj):
      self.postGroupID:str = obj["postGroupID"]
      """  The Group ID of the Group to post  """  
      pass

class DeleteZeroAmtTaxRec_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CashGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this. This value is then duplicated into the CashHead and CashDtl as part of the Post process. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period. This is then duplicated into the CashHead and CashDtl during posting process.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Related record to a  BankAcct.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  If yes, indicates that the group is for Payment Instrument.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  Flag indicating payments were processed  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Payment Instrument Status  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  Indicates its a PI Status Change group  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalApplied:int = obj["TotalApplied"]
      self.UnappliedBalance:int = obj["UnappliedBalance"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.TotalDeposit:int = obj["TotalDeposit"]
      self.TotalMisc:int = obj["TotalMisc"]
      self.TotalARAmount:int = obj["TotalARAmount"]
      self.TotalWithhold:int = obj["TotalWithhold"]
      self.PostErrorLog:str = obj["PostErrorLog"]
      self.PostToGL:bool = obj["PostToGL"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BankCurrencyCodeDocumentDesc:str = obj["BankCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BankCurrencyCodeCurrencyID:str = obj["BankCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BankCurrencyCodeCurrName:str = obj["BankCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BankCurrencyCodeCurrDesc:str = obj["BankCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.BankCurrencyCodeCurrSymbol:str = obj["BankCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.PMType:int = obj["PMType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.PMName:str = obj["PMName"]
      """  Name of the payment method  """  
      self.PMSummarizePerCustomer:bool = obj["PMSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.TotalWriteOff:int = obj["TotalWriteOff"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashGrpListTableset:
   def __init__(self, obj):
      self.CashGrpList:list[Erp_Tablesets_CashGrpListRow] = obj["CashGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this. This value is then duplicated into the CashHead and CashDtl as part of the Post process. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period. This is then duplicated into the CashHead and CashDtl during posting process.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Related record to a  BankAcct.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  If yes, indicates that the group is for Payment Instrument.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  Flag indicating payments were processed  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Payment Instrument Status  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  Indicates its a PI Status Change group  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Auto Generated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.BankCurrencyCodeCurrDesc:str = obj["BankCurrencyCodeCurrDesc"]
      self.BankCurrencyCodeCurrencyID:str = obj["BankCurrencyCodeCurrencyID"]
      self.BankCurrencyCodeCurrName:str = obj["BankCurrencyCodeCurrName"]
      self.BankCurrencyCodeCurrSymbol:str = obj["BankCurrencyCodeCurrSymbol"]
      self.BankCurrencyCodeDocumentDesc:str = obj["BankCurrencyCodeDocumentDesc"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DepSlipGrouping:bool = obj["DepSlipGrouping"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      self.EIGrouping:bool = obj["EIGrouping"]
      self.PostErrorLog:str = obj["PostErrorLog"]
      self.PostToGL:bool = obj["PostToGL"]
      self.TotalApplied:int = obj["TotalApplied"]
      self.TotalARAmount:int = obj["TotalARAmount"]
      self.TotalBankFee:int = obj["TotalBankFee"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalDeposit:int = obj["TotalDeposit"]
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.TotalMisc:int = obj["TotalMisc"]
      self.TotalWithhold:int = obj["TotalWithhold"]
      self.UIGrouping:bool = obj["UIGrouping"]
      self.UnappliedBalance:int = obj["UnappliedBalance"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.TotalWriteOff:int = obj["TotalWriteOff"]
      self.IsDocumentLocked:bool = obj["IsDocumentLocked"]
      """  Shows that the group contains payments which are in review  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: a payment is already in review journal or in posting process.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.PIStatusPIStage:str = obj["PIStatusPIStage"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PMARIDTiming:int = obj["PMARIDTiming"]
      self.PMName:str = obj["PMName"]
      self.PMType:int = obj["PMType"]
      self.PMSummarizePerCustomer:bool = obj["PMSummarizePerCustomer"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashGrpTableset:
   def __init__(self, obj):
      self.CashGrp:list[Erp_Tablesets_CashGrpRow] = obj["CashGrp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCashGrpTableset:
   def __init__(self, obj):
      self.CashGrp:list[Erp_Tablesets_CashGrpRow] = obj["CashGrp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDNoLock_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByIDNoLock_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetGrpBankInfo_input:
   """ Required : 
   BankAcctId
   ds
   """  
   def __init__(self, obj):
      self.BankAcctId:str = obj["BankAcctId"]
      """  Proposed Bank Account  """  
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GetGrpBankInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetGrpFiscal_input:
   """ Required : 
   tranDate
   ds
   """  
   def __init__(self, obj):
      self.tranDate:str = obj["tranDate"]
      """  Proposed Transaction Date  """  
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GetGrpFiscal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListDepositSlips_input:
   """ Required : 
   whereClause
   bankAcctID
   groupIDs
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  whereClause  """  
      self.bankAcctID:str = obj["bankAcctID"]
      self.groupIDs:str = obj["groupIDs"]
      """  list of group IDs  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListDepositSlips_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_CashGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCashGrpForPINoLock_input:
   """ Required : 
   ipStage
   ds
   """  
   def __init__(self, obj):
      self.ipStage:str = obj["ipStage"]
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GetNewCashGrpForPINoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashGrpForPIStatusNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GetNewCashGrpForPIStatusNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashGrpForPIStatus_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GetNewCashGrpForPIStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashGrpForPI_input:
   """ Required : 
   ipStage
   ds
   """  
   def __init__(self, obj):
      self.ipStage:str = obj["ipStage"]
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GetNewCashGrpForPI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashGrpNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GetNewCashGrpNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GetNewCashGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPIGroupByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Selected Group ID  """  
      pass

class GetPIGroupByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
      pass

class GetPIStatusGroupByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Selected Group ID  """  
      pass

class GetPIStatusGroupByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
      pass

class GetRowsNoLock_input:
   """ Required : 
   whereClauseCashGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashGrp:str = obj["whereClauseCashGrp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsNoLock_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsUseLockSetting_input:
   """ Required : 
   whereClauseCashGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashGrp:str = obj["whereClauseCashGrp"]
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsUseLockSetting_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCashGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashGrp:str = obj["whereClauseCashGrp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GroupLock_input:
   """ Required : 
   groupID
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID to lock  """  
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GroupLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GroupUnlock_input:
   """ Required : 
   groupID
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID.  """  
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class GroupUnlock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
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

class IsPIGroup_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class IsPIGroup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.promissoryNote:bool = obj["promissoryNote"]
      self.piStatusGrp:bool = obj["piStatusGrp"]
      self.cashbook:bool = obj["cashbook"]
      pass

      """  output parameters  """  

class LeaveCashGrp_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Cash Group ID to clear  """  
      pass

class LeaveCashGrp_output:
   def __init__(self, obj):
      pass

class LockPIGroupInDS_input:
   """ Required : 
   groupID
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Selected Group ID  """  
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class LockPIGroupInDS_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LockPIGroup_input:
   """ Required : 
   groupID
   PIStatusGrp
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Selected Group ID  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  True only if it is PI Status Change Group Type  """  
      pass

class LockPIGroup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class PrePostEPGroup_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Cash Group ID to check if it was processed  """  
      pass

class PrePostEPGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vQuestion:str = obj["parameters"]
      self.vTaxQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class PrePostGroup_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Cash Group ID to check if it was processed  """  
      pass

class PrePostGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vQuestion:str = obj["parameters"]
      self.vTaxQuestion:str = obj["parameters"]
      self.lnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReceiptGroupExists_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      pass

class ReceiptGroupExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UnlockPIGroupInDS_input:
   """ Required : 
   pcGroupID
   ds
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  The Group ID selected by the user.  """  
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class UnlockPIGroupInDS_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnlockPIGroup_input:
   """ Required : 
   pcGroupID
   PIStatusGrp
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  The Group ID selected by the user.  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  Is PIStatusGrp  """  
      pass

class UnlockPIGroup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCashGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCashGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateMaster_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class UpdateMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      self.mode:int = obj["parameters"]
      self.oldBankBatchSysRowID:str = obj["parameters"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

