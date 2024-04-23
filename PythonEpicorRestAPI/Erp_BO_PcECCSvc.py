import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PcECCSvc
# Description: Pc ECC main object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PcECCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcECCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcECCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcECCOrderDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs",headers=creds) as resp:
           return await resp.json()

async def post_PcECCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcECCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcECCOrderDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcECCOrderDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcECCs_Company_ECCBSVID(Company, ECCBSVID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcECC item
   Description: Calls GetByID to retrieve the PcECC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcECC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECCBSVID: Desc: ECCBSVID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcECCOrderDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs(" + Company + "," + ECCBSVID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcECCs_Company_ECCBSVID(Company, ECCBSVID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcECC for the service
   Description: Calls UpdateExt to update PcECC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcECC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECCBSVID: Desc: ECCBSVID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcECCOrderDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs(" + Company + "," + ECCBSVID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcECCs_Company_ECCBSVID(Company, ECCBSVID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcECC item
   Description: Call UpdateExt to delete PcECC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcECC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECCBSVID: Desc: ECCBSVID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs(" + Company + "," + ECCBSVID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcECCOrderDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePcECCOrderDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePcECCOrderDtl=" + whereClausePcECCOrderDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(ecCBSVID, epicorHeaders = None):
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
   params += "ecCBSVID=" + ecCBSVID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_SubmitCIMRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitCIMRequest
   Description: Creates/updates PcECCOrderDtl record to be used later by EWA
   OperationID: SubmitCIMRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitCIMRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitCIMRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBasePartForConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBasePartForConfig
   Description: This method will retrieve the base configured part number to be passed
to configuration entry
   OperationID: GetBasePartForConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartForConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartForConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetKBMaxConfigProdID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetKBMaxConfigProdID
   Description: Set the CPQ Quote Product ID on the Web Basket Line.
   OperationID: SetKBMaxConfigProdID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetKBMaxConfigProdID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetKBMaxConfigProdID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcECCOrderDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcECCOrderDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcECCOrderDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcECCOrderDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcECCOrderDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcECCOrderDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcECCOrderDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcECCOrderDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcECCOrderDtlRow] = obj["value"]
      pass

class Erp_Tablesets_PcECCOrderDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ECCBSVID:str = obj["ECCBSVID"]
      """  ECCBSVID  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  BasePartNum  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  BaseRevisionNum  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.LineDesc:str = obj["LineDesc"]
      """  LineDesc  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  BreakListCode  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Commissionable  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      """  DiscBreakListCode  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  LockPrice  """  
      self.LockQty:bool = obj["LockQty"]
      """  LockQty  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.OrderComment:str = obj["OrderComment"]
      """  OrderComment  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      """  OverrideDiscPriceList  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  OverridePriceList  """  
      self.PickListComment:str = obj["PickListComment"]
      """  PickListComment  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  PricePerCode  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.RequestDate:str = obj["RequestDate"]
      """  RequestDate  """  
      self.Rework:bool = obj["Rework"]
      """  Rework  """  
      self.RMALine:int = obj["RMALine"]
      """  RMALine  """  
      self.RMANum:int = obj["RMANum"]
      """  RMANum  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  SellingQuantity  """  
      self.ShipComment:str = obj["ShipComment"]
      """  ShipComment  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  ShipLineComplete  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  TaxCatID  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  TMBilling  """  
      self.XPartNum:str = obj["XPartNum"]
      """  XPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  XRevisionNum  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  DocUnitPrice  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  ConfigBaseUnitPrice  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """  ConfigUnitPrice  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcECCOrderDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ECCBSVID:str = obj["ECCBSVID"]
      """  ECCBSVID  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  BasePartNum  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  BaseRevisionNum  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.LineDesc:str = obj["LineDesc"]
      """  LineDesc  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  BreakListCode  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Commissionable  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      """  DiscBreakListCode  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  LockPrice  """  
      self.LockQty:bool = obj["LockQty"]
      """  LockQty  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.OrderComment:str = obj["OrderComment"]
      """  OrderComment  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      """  OverrideDiscPriceList  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  OverridePriceList  """  
      self.PickListComment:str = obj["PickListComment"]
      """  PickListComment  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  PricePerCode  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.RequestDate:str = obj["RequestDate"]
      """  RequestDate  """  
      self.Rework:bool = obj["Rework"]
      """  Rework  """  
      self.RMALine:int = obj["RMALine"]
      """  RMALine  """  
      self.RMANum:int = obj["RMANum"]
      """  RMANum  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  SellingQuantity  """  
      self.ShipComment:str = obj["ShipComment"]
      """  ShipComment  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  ShipLineComplete  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  TaxCatID  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  TMBilling  """  
      self.XPartNum:str = obj["XPartNum"]
      """  XPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  XRevisionNum  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  DocUnitPrice  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  ConfigBaseUnitPrice  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """  ConfigUnitPrice  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECCQuoteNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  AnalysisCode  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  BestCsPct  """  
      self.Discount:int = obj["Discount"]
      """  Discount  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  DiscountPercent  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  DocDiscount  """  
      self.Engineer:bool = obj["Engineer"]
      """  Engineer  """  
      self.JobComment:str = obj["JobComment"]
      """  JobComment  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  KitQtyPer  """  
      self.LeadTime:str = obj["LeadTime"]
      """  LeadTime  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  MultiRel  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  QuoteComment  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  ReqShipDate  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  SellingExpectedQty  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  SellingExpectedUM  """  
      self.Template:bool = obj["Template"]
      """  Template  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  WorstCsPct  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.MSRP:int = obj["MSRP"]
      """  MSRP  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  EndCustomerPrice  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate.  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.ConfigID:str = obj["ConfigID"]
      self.ConfigVersion:int = obj["ConfigVersion"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   ecCBSVID
   """  
   def __init__(self, obj):
      self.ecCBSVID:str = obj["ecCBSVID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PcECCListTableset:
   def __init__(self, obj):
      self.PcECCOrderDtlList:list[Erp_Tablesets_PcECCOrderDtlListRow] = obj["PcECCOrderDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcECCOrderDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ECCBSVID:str = obj["ECCBSVID"]
      """  ECCBSVID  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  BasePartNum  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  BaseRevisionNum  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.LineDesc:str = obj["LineDesc"]
      """  LineDesc  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  BreakListCode  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Commissionable  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      """  DiscBreakListCode  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  LockPrice  """  
      self.LockQty:bool = obj["LockQty"]
      """  LockQty  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.OrderComment:str = obj["OrderComment"]
      """  OrderComment  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      """  OverrideDiscPriceList  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  OverridePriceList  """  
      self.PickListComment:str = obj["PickListComment"]
      """  PickListComment  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  PricePerCode  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.RequestDate:str = obj["RequestDate"]
      """  RequestDate  """  
      self.Rework:bool = obj["Rework"]
      """  Rework  """  
      self.RMALine:int = obj["RMALine"]
      """  RMALine  """  
      self.RMANum:int = obj["RMANum"]
      """  RMANum  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  SellingQuantity  """  
      self.ShipComment:str = obj["ShipComment"]
      """  ShipComment  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  ShipLineComplete  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  TaxCatID  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  TMBilling  """  
      self.XPartNum:str = obj["XPartNum"]
      """  XPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  XRevisionNum  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  DocUnitPrice  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  ConfigBaseUnitPrice  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """  ConfigUnitPrice  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcECCOrderDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ECCBSVID:str = obj["ECCBSVID"]
      """  ECCBSVID  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  BasePartNum  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  BaseRevisionNum  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.LineDesc:str = obj["LineDesc"]
      """  LineDesc  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  BreakListCode  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Commissionable  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      """  DiscBreakListCode  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  LockPrice  """  
      self.LockQty:bool = obj["LockQty"]
      """  LockQty  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.OrderComment:str = obj["OrderComment"]
      """  OrderComment  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      """  OverrideDiscPriceList  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  OverridePriceList  """  
      self.PickListComment:str = obj["PickListComment"]
      """  PickListComment  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  PricePerCode  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.RequestDate:str = obj["RequestDate"]
      """  RequestDate  """  
      self.Rework:bool = obj["Rework"]
      """  Rework  """  
      self.RMALine:int = obj["RMALine"]
      """  RMALine  """  
      self.RMANum:int = obj["RMANum"]
      """  RMANum  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  SellingQuantity  """  
      self.ShipComment:str = obj["ShipComment"]
      """  ShipComment  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  ShipLineComplete  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  TaxCatID  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  TMBilling  """  
      self.XPartNum:str = obj["XPartNum"]
      """  XPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  XRevisionNum  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  DocUnitPrice  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  ConfigBaseUnitPrice  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """  ConfigUnitPrice  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECCQuoteNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  AnalysisCode  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  BestCsPct  """  
      self.Discount:int = obj["Discount"]
      """  Discount  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  DiscountPercent  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  DocDiscount  """  
      self.Engineer:bool = obj["Engineer"]
      """  Engineer  """  
      self.JobComment:str = obj["JobComment"]
      """  JobComment  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  KitQtyPer  """  
      self.LeadTime:str = obj["LeadTime"]
      """  LeadTime  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  MultiRel  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  QuoteComment  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  ReqShipDate  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  SellingExpectedQty  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  SellingExpectedUM  """  
      self.Template:bool = obj["Template"]
      """  Template  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  WorstCsPct  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.MSRP:int = obj["MSRP"]
      """  MSRP  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  EndCustomerPrice  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate.  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.ConfigID:str = obj["ConfigID"]
      self.ConfigVersion:int = obj["ConfigVersion"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcECCTableset:
   def __init__(self, obj):
      self.PcECCOrderDtl:list[Erp_Tablesets_PcECCOrderDtlRow] = obj["PcECCOrderDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPcECCTableset:
   def __init__(self, obj):
      self.PcECCOrderDtl:list[Erp_Tablesets_PcECCOrderDtlRow] = obj["PcECCOrderDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetBasePartForConfig_input:
   """ Required : 
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      """  Order Number of the target Assembly  """  
      pass

class GetBasePartForConfig_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   ecCBSVID
   """  
   def __init__(self, obj):
      self.ecCBSVID:str = obj["ecCBSVID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcECCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PcECCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PcECCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PcECCListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPcECCOrderDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcECCTableset] = obj["ds"]
      pass

class GetNewPcECCOrderDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcECCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePcECCOrderDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePcECCOrderDtl:str = obj["whereClausePcECCOrderDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcECCTableset] = obj["returnObj"]
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

class SetKBMaxConfigProdID_input:
   """ Required : 
   eccBsvID
   kbConfigProdID
   """  
   def __init__(self, obj):
      self.eccBsvID:str = obj["eccBsvID"]
      """  Web Basket ID  """  
      self.kbConfigProdID:int = obj["kbConfigProdID"]
      """  CPQ Quote Product ID  """  
      pass

class SetKBMaxConfigProdID_output:
   def __init__(self, obj):
      pass

class SubmitCIMRequest_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcECCTableset] = obj["ds"]
      pass

class SubmitCIMRequest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcECCTableset] = obj["ds"]
      self.errCode:str = obj["parameters"]
      self.errMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPcECCTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPcECCTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcECCTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcECCTableset] = obj["ds"]
      pass

      """  output parameters  """  

