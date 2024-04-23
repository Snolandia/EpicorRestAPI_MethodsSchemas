import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CNCustomsDeclBillDtlSearchSvc
# Description: Customs Declaration Bill Line Search Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsDeclBillDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CNCustomsDeclBillDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNCustomsDeclBillDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsDeclBillDtlSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/CNCustomsDeclBillDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_CNCustomsDeclBillDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNCustomsDeclBillDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclBillDtlSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclBillDtlSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/CNCustomsDeclBillDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CNCustomsDeclBillDtlSearches_Company_DeclarationBill_DeclarationBillLine(Company, DeclarationBill, DeclarationBillLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CNCustomsDeclBillDtlSearch item
   Description: Calls GetByID to retrieve the CNCustomsDeclBillDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNCustomsDeclBillDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
      :param DeclarationBillLine: Desc: DeclarationBillLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclBillDtlSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/CNCustomsDeclBillDtlSearches(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CNCustomsDeclBillDtlSearches_Company_DeclarationBill_DeclarationBillLine(Company, DeclarationBill, DeclarationBillLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CNCustomsDeclBillDtlSearch for the service
   Description: Calls UpdateExt to update CNCustomsDeclBillDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNCustomsDeclBillDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
      :param DeclarationBillLine: Desc: DeclarationBillLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNCustomsDeclBillDtlSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/CNCustomsDeclBillDtlSearches(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CNCustomsDeclBillDtlSearches_Company_DeclarationBill_DeclarationBillLine(Company, DeclarationBill, DeclarationBillLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CNCustomsDeclBillDtlSearch item
   Description: Call UpdateExt to delete CNCustomsDeclBillDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNCustomsDeclBillDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationBill: Desc: DeclarationBill   Required: True   Allow empty value : True
      :param DeclarationBillLine: Desc: DeclarationBillLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/CNCustomsDeclBillDtlSearches(" + Company + "," + DeclarationBill + "," + DeclarationBillLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNCustomsDeclBillDtlSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCNCustomsDeclBillDtlSearch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCNCustomsDeclBillDtlSearch=" + whereClauseCNCustomsDeclBillDtlSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(declarationBill, declarationBillLine, epicorHeaders = None):
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
   params += "declarationBill=" + declarationBill
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "declarationBillLine=" + declarationBillLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsOfSrcDocumentType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsOfSrcDocumentType
   Description: Invokes GetRows filtering on Invoices for the specified Quote
   OperationID: GetRowsOfSrcDocumentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsOfSrcDocumentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsOfSrcDocumentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCNCustomsDeclBillDtlSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCNCustomsDeclBillDtlSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCNCustomsDeclBillDtlSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCNCustomsDeclBillDtlSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCNCustomsDeclBillDtlSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNCustomsDeclBillDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclBillDtlSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNCustomsDeclBillDtlSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchRow] = obj["value"]
      pass

class Erp_Tablesets_CNCustomsDeclBillDtlSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.DeclarationBillLine:int = obj["DeclarationBillLine"]
      """  Line Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price  """  
      self.TotalPrice:int = obj["TotalPrice"]
      """  Total Price  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country  """  
      self.DomesticDestination:str = obj["DomesticDestination"]
      """  Domestic Destination  """  
      self.TaxExemptType:str = obj["TaxExemptType"]
      """  Tax Exemption Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsDeclBillDtlSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.DeclarationBillLine:int = obj["DeclarationBillLine"]
      """  Line Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price  """  
      self.TotalPrice:int = obj["TotalPrice"]
      """  Total Price  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country  """  
      self.DomesticDestination:str = obj["DomesticDestination"]
      """  Domestic Destination  """  
      self.TaxExemptType:str = obj["TaxExemptType"]
      """  Tax Exemption Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   declarationBill
   declarationBillLine
   """  
   def __init__(self, obj):
      self.declarationBill:str = obj["declarationBill"]
      self.declarationBillLine:int = obj["declarationBillLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CNCustomsDeclBillDtlSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.DeclarationBillLine:int = obj["DeclarationBillLine"]
      """  Line Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price  """  
      self.TotalPrice:int = obj["TotalPrice"]
      """  Total Price  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country  """  
      self.DomesticDestination:str = obj["DomesticDestination"]
      """  Domestic Destination  """  
      self.TaxExemptType:str = obj["TaxExemptType"]
      """  Tax Exemption Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsDeclBillDtlSearchListTableset:
   def __init__(self, obj):
      self.CNCustomsDeclBillDtlSearchList:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchListRow] = obj["CNCustomsDeclBillDtlSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CNCustomsDeclBillDtlSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeclarationBill:str = obj["DeclarationBill"]
      """  Declaration Bill  """  
      self.DeclarationBillLine:int = obj["DeclarationBillLine"]
      """  Line Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Weight  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price  """  
      self.TotalPrice:int = obj["TotalPrice"]
      """  Total Price  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country  """  
      self.DomesticDestination:str = obj["DomesticDestination"]
      """  Domestic Destination  """  
      self.TaxExemptType:str = obj["TaxExemptType"]
      """  Tax Exemption Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset:
   def __init__(self, obj):
      self.CNCustomsDeclBillDtlSearch:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchRow] = obj["CNCustomsDeclBillDtlSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCNCustomsDeclBillDtlSearchTableset:
   def __init__(self, obj):
      self.CNCustomsDeclBillDtlSearch:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchRow] = obj["CNCustomsDeclBillDtlSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   declarationBill
   declarationBillLine
   """  
   def __init__(self, obj):
      self.declarationBill:str = obj["declarationBill"]
      self.declarationBillLine:int = obj["declarationBillLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCNCustomsDeclBillDtlSearch_input:
   """ Required : 
   ds
   declarationBill
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["ds"]
      self.declarationBill:str = obj["declarationBill"]
      pass

class GetNewCNCustomsDeclBillDtlSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsOfSrcDocumentType_input:
   """ Required : 
   whereClauseCNCustomsDeclBillDtlSearch
   sourceDocumentType
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCNCustomsDeclBillDtlSearch:str = obj["whereClauseCNCustomsDeclBillDtlSearch"]
      self.sourceDocumentType:str = obj["sourceDocumentType"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsOfSrcDocumentType_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCNCustomsDeclBillDtlSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCNCustomsDeclBillDtlSearch:str = obj["whereClauseCNCustomsDeclBillDtlSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCNCustomsDeclBillDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNCustomsDeclBillDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNCustomsDeclBillDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

