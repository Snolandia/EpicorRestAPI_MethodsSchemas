import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ServiceContractSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContractSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ServiceContractSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ServiceContractSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ServiceContractSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches",headers=creds) as resp:
           return await resp.json()

async def post_ServiceContractSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ServiceContractSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ServiceContractSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ServiceContractSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ServiceContractSearches_Company_ContractNum(Company, ContractNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ServiceContractSearch item
   Description: Calls GetByID to retrieve the ServiceContractSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ServiceContractSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ServiceContractSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches(" + Company + "," + ContractNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ServiceContractSearches_Company_ContractNum(Company, ContractNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ServiceContractSearch for the service
   Description: Calls UpdateExt to update ServiceContractSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ServiceContractSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ServiceContractSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches(" + Company + "," + ContractNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ServiceContractSearches_Company_ContractNum(Company, ContractNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ServiceContractSearch item
   Description: Call UpdateExt to delete ServiceContractSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ServiceContractSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches(" + Company + "," + ContractNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ServiceContractSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseServiceContractSearch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseServiceContractSearch=" + whereClauseServiceContractSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(contractNum, epicorHeaders = None):
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
   params += "contractNum=" + contractNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetContractsRenewalsLP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractsRenewalsLP
   Description: Returns the service contracts as the GetRows does.
   OperationID: GetContractsRenewalsLP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractsRenewalsLP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractsRenewalsLP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractsRenewalsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractsRenewalsList
   Description: Returns the service contracts List  but with the option of filtering by the ones with renewals
   OperationID: GetContractsRenewalsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractsRenewalsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractsRenewalsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractsRenewals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractsRenewals
   Description: Returns the service contracts as the GetRows does but filtering them out by one with renewals
   OperationID: GetContractsRenewals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractsRenewals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractsRenewals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: Custom GetList method.
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewServiceContractSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewServiceContractSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewServiceContractSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewServiceContractSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewServiceContractSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ServiceContractSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ServiceContractSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ServiceContractSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ServiceContractSearchRow] = obj["value"]
      pass

class Erp_Tablesets_ServiceContractSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.ContractType:str = obj["ContractType"]
      """  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ContVoid:bool = obj["ContVoid"]
      """  This Service Contract has been deactivated when TRUE  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country Number.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.Suspended:bool = obj["Suspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.QuotedContract:bool = obj["QuotedContract"]
      """  Indicates if the contrct will automatically generate a quote  """  
      self.ShipContract:bool = obj["ShipContract"]
      """  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractLine:int = obj["ContractLine"]
      self.ContractQty:int = obj["ContractQty"]
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      self.IUM:str = obj["IUM"]
      self.LineDesc:str = obj["LineDesc"]
      self.PartNum:str = obj["PartNum"]
      self.PricePerUnit:int = obj["PricePerUnit"]
      self.ProdCode:str = obj["ProdCode"]
      self.ProjectID:str = obj["ProjectID"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.XPartNum:str = obj["XPartNum"]
      self.XRevisionNum:str = obj["XRevisionNum"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ServiceContractSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.ContractType:str = obj["ContractType"]
      """  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ContVoid:bool = obj["ContVoid"]
      """  This Service Contract has been deactivated when TRUE  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country Number.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.Suspended:bool = obj["Suspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.QuotedContract:bool = obj["QuotedContract"]
      """  Indicates if the contrct will automatically generate a quote  """  
      self.ShipContract:bool = obj["ShipContract"]
      """  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvcTiming:str = obj["InvcTiming"]
      """  InvcTiming  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Indicates how often an invoice is generated for the contract.  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract using is valid for renewal.  """  
      self.IncIntrastat:bool = obj["IncIntrastat"]
      """  Intrastat: Activates HS Commodity code retrieving in contract invoicing  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the service contract has to be synchronized with Epicor FSA application.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.ContractQty:int = obj["ContractQty"]
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      self.IUM:str = obj["IUM"]
      self.LineDesc:str = obj["LineDesc"]
      self.PartNum:str = obj["PartNum"]
      self.PricePerUnit:int = obj["PricePerUnit"]
      self.ProdCode:str = obj["ProdCode"]
      self.ProjectID:str = obj["ProjectID"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.XPartNum:str = obj["XPartNum"]
      self.XRevisionNum:str = obj["XRevisionNum"]
      self.ContractLine:int = obj["ContractLine"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   contractNum
   """  
   def __init__(self, obj):
      self.contractNum:int = obj["contractNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ServiceContractSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.ContractType:str = obj["ContractType"]
      """  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ContVoid:bool = obj["ContVoid"]
      """  This Service Contract has been deactivated when TRUE  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country Number.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.Suspended:bool = obj["Suspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.QuotedContract:bool = obj["QuotedContract"]
      """  Indicates if the contrct will automatically generate a quote  """  
      self.ShipContract:bool = obj["ShipContract"]
      """  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractLine:int = obj["ContractLine"]
      self.ContractQty:int = obj["ContractQty"]
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      self.IUM:str = obj["IUM"]
      self.LineDesc:str = obj["LineDesc"]
      self.PartNum:str = obj["PartNum"]
      self.PricePerUnit:int = obj["PricePerUnit"]
      self.ProdCode:str = obj["ProdCode"]
      self.ProjectID:str = obj["ProjectID"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.XPartNum:str = obj["XPartNum"]
      self.XRevisionNum:str = obj["XRevisionNum"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ServiceContractSearchListTableset:
   def __init__(self, obj):
      self.ServiceContractSearchList:list[Erp_Tablesets_ServiceContractSearchListRow] = obj["ServiceContractSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ServiceContractSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.ContractType:str = obj["ContractType"]
      """  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ContVoid:bool = obj["ContVoid"]
      """  This Service Contract has been deactivated when TRUE  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country Number.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.Suspended:bool = obj["Suspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.QuotedContract:bool = obj["QuotedContract"]
      """  Indicates if the contrct will automatically generate a quote  """  
      self.ShipContract:bool = obj["ShipContract"]
      """  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvcTiming:str = obj["InvcTiming"]
      """  InvcTiming  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Indicates how often an invoice is generated for the contract.  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract using is valid for renewal.  """  
      self.IncIntrastat:bool = obj["IncIntrastat"]
      """  Intrastat: Activates HS Commodity code retrieving in contract invoicing  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the service contract has to be synchronized with Epicor FSA application.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.ContractQty:int = obj["ContractQty"]
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      self.IUM:str = obj["IUM"]
      self.LineDesc:str = obj["LineDesc"]
      self.PartNum:str = obj["PartNum"]
      self.PricePerUnit:int = obj["PricePerUnit"]
      self.ProdCode:str = obj["ProdCode"]
      self.ProjectID:str = obj["ProjectID"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.XPartNum:str = obj["XPartNum"]
      self.XRevisionNum:str = obj["XRevisionNum"]
      self.ContractLine:int = obj["ContractLine"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ServiceContractSearchTableset:
   def __init__(self, obj):
      self.ServiceContractSearch:list[Erp_Tablesets_ServiceContractSearchRow] = obj["ServiceContractSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtServiceContractSearchTableset:
   def __init__(self, obj):
      self.ServiceContractSearch:list[Erp_Tablesets_ServiceContractSearchRow] = obj["ServiceContractSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   contractNum
   """  
   def __init__(self, obj):
      self.contractNum:int = obj["contractNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["returnObj"]
      pass

class GetContractsRenewalsLP_input:
   """ Required : 
   whereClause
   statusFilter
   renewalsOnly
   startingAt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The where clause used to filter the records.  """  
      self.statusFilter:str = obj["statusFilter"]
      """  Status Filter, options "All,Active, Expired"  """  
      self.renewalsOnly:bool = obj["renewalsOnly"]
      """  Indicates if only those contracts with renewals are returned  """  
      self.startingAt:str = obj["startingAt"]
      """  The Starting At and Sort used in the Search.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetContractsRenewalsLP_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetContractsRenewalsList_input:
   """ Required : 
   ContractNumberFilter
   filter
   renewalsOnly
   parentWhereClause
   SortByClause
   PartDescContains
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ContractNumberFilter:str = obj["ContractNumberFilter"]
      """  To be use if no "SortBy" haven provided  """  
      self.filter:str = obj["filter"]
      """  Status Filter, options "All,Active, Expired"  """  
      self.renewalsOnly:bool = obj["renewalsOnly"]
      """  Indicates if only those contracts with renewals are returned  """  
      self.parentWhereClause:str = obj["parentWhereClause"]
      """  WhereClause to filter the Parent records.  """  
      self.SortByClause:str = obj["SortByClause"]
      """  To sort by the detail records.  """  
      self.PartDescContains:str = obj["PartDescContains"]
      """  The part contains filter  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetContractsRenewalsList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetContractsRenewals_input:
   """ Required : 
   renewalsOnly
   WhereClause
   SortByClause
   PartDescContains
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.renewalsOnly:bool = obj["renewalsOnly"]
      """  Indicates if only those contracts with renewals are returned  """  
      self.WhereClause:str = obj["WhereClause"]
      """  WhereClause to filter the Parent records.  """  
      self.SortByClause:str = obj["SortByClause"]
      """  To sort by the detail records.  """  
      self.PartDescContains:str = obj["PartDescContains"]
      """  The part contains filter  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetContractsRenewals_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListCustom_input:
   """ Required : 
   WhereClause
   SortByClause
   PartDescContains
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      """  WhereClause to filter the Parent records.  """  
      self.SortByClause:str = obj["SortByClause"]
      """  To sort by the detail records.  """  
      self.PartDescContains:str = obj["PartDescContains"]
      """  The part contains filter  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewServiceContractSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["ds"]
      pass

class GetNewServiceContractSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   WhereClause
   SortByClause
   PartDescContains
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      """  WhereClause to filter the Parent records.  """  
      self.SortByClause:str = obj["SortByClause"]
      """  To sort by the detail records.  """  
      self.PartDescContains:str = obj["PartDescContains"]
      """  The part contains filter  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseServiceContractSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseServiceContractSearch:str = obj["whereClauseServiceContractSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtServiceContractSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtServiceContractSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

