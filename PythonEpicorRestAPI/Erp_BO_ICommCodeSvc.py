import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ICommCodeSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ICommCodes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ICommCodes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ICommCodes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ICommCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/ICommCodes",headers=creds) as resp:
           return await resp.json()

async def post_ICommCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ICommCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ICommCodeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ICommCodeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/ICommCodes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ICommCodes_Company_CommodityCode(Company, CommodityCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ICommCode item
   Description: Calls GetByID to retrieve the ICommCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ICommCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CommodityCode: Desc: CommodityCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ICommCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/ICommCodes(" + Company + "," + CommodityCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ICommCodes_Company_CommodityCode(Company, CommodityCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ICommCode for the service
   Description: Calls UpdateExt to update ICommCode. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ICommCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CommodityCode: Desc: CommodityCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ICommCodeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/ICommCodes(" + Company + "," + CommodityCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ICommCodes_Company_CommodityCode(Company, CommodityCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ICommCode item
   Description: Call UpdateExt to delete ICommCode item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ICommCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CommodityCode: Desc: CommodityCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/ICommCodes(" + Company + "," + CommodityCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ICommCodeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseICommCode, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseICommCode=" + whereClauseICommCode
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(commodityCode, epicorHeaders = None):
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
   params += "commodityCode=" + commodityCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewICommCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewICommCode
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewICommCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewICommCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewICommCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ICommCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ICommCodeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ICommCodeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ICommCodeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ICommCodeRow] = obj["value"]
      pass

class Erp_Tablesets_ICommCodeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.Description:str = obj["Description"]
      """  Full description of the Commodity Code.  """  
      self.RequiresWeight:bool = obj["RequiresWeight"]
      """  For most Intrastat commodity codes, the weight does not need to be reported. A TRUE value for this field, indicates that the weight is needed for Intrastat reporting. Posting of invoices may be blocked (ISSyst.BlockWeight) if there exists a line with a required weight equal to zero.  """  
      self.RequiresUM:bool = obj["RequiresUM"]
      """  For most Intrastat commodity codes, the UM (or "Supplementary Unit") does not need to be reported. A TRUE value for this field, indicates that a secondary quantity is needed for Intrastat reporting.  """  
      self.NotReported:bool = obj["NotReported"]
      """  Indicates if the commodity code does not need to be reported on Intrastat reports.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StatImportCode:str = obj["StatImportCode"]
      """  Optional field to store the Statistical Import Code.  For reporting purposes only.  """  
      self.StatExportCode:str = obj["StatExportCode"]
      """  Optional field to store the Statistical Export Code.  For reporting purposes only.  """  
      self.ImportCode:str = obj["ImportCode"]
      """  Optional field to store the Import Code.  For reporting purposes only.  """  
      self.ExportCode:str = obj["ExportCode"]
      """  Optional field to store the Export Code.  For reporting purposes only.  """  
      self.GlobalICommCode:bool = obj["GlobalICommCode"]
      """  Marks this ICommCode as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Intrastat:bool = obj["Intrastat"]
      """  True if Intrastat is enabled in company  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ICommCodeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.Description:str = obj["Description"]
      """  Full description of the Commodity Code.  """  
      self.RequiresWeight:bool = obj["RequiresWeight"]
      """  For most Intrastat commodity codes, the weight does not need to be reported. A TRUE value for this field, indicates that the weight is needed for Intrastat reporting. Posting of invoices may be blocked (ISSyst.BlockWeight) if there exists a line with a required weight equal to zero.  """  
      self.RequiresUM:bool = obj["RequiresUM"]
      """  For most Intrastat commodity codes, the UM (or "Supplementary Unit") does not need to be reported. A TRUE value for this field, indicates that a secondary quantity is needed for Intrastat reporting.  """  
      self.NotReported:bool = obj["NotReported"]
      """  Indicates if the commodity code does not need to be reported on Intrastat reports.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StatImportCode:str = obj["StatImportCode"]
      """  Optional field to store the Statistical Import Code.  For reporting purposes only.  """  
      self.StatExportCode:str = obj["StatExportCode"]
      """  Optional field to store the Statistical Export Code.  For reporting purposes only.  """  
      self.ImportCode:str = obj["ImportCode"]
      """  Optional field to store the Import Code.  For reporting purposes only.  """  
      self.ExportCode:str = obj["ExportCode"]
      """  Optional field to store the Export Code.  For reporting purposes only.  """  
      self.GlobalICommCode:bool = obj["GlobalICommCode"]
      """  Marks this ICommCode as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SuppUnitsUOM:str = obj["SuppUnitsUOM"]
      """  SuppUnitsUOM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCustomsTaxRate:int = obj["CNCustomsTaxRate"]
      """  Customs Duty Rate  """  
      self.CNDescription:str = obj["CNDescription"]
      """  CN Description  """  
      self.TaricCode:str = obj["TaricCode"]
      """  European Union integrated tariff.  """  
      self.EUPreference:str = obj["EUPreference"]
      """  European Union preference.  """  
      self.Intrastat:bool = obj["Intrastat"]
      """  True if Intrastat is enabled in company  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   commodityCode
   """  
   def __init__(self, obj):
      self.commodityCode:str = obj["commodityCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ICommCodeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.Description:str = obj["Description"]
      """  Full description of the Commodity Code.  """  
      self.RequiresWeight:bool = obj["RequiresWeight"]
      """  For most Intrastat commodity codes, the weight does not need to be reported. A TRUE value for this field, indicates that the weight is needed for Intrastat reporting. Posting of invoices may be blocked (ISSyst.BlockWeight) if there exists a line with a required weight equal to zero.  """  
      self.RequiresUM:bool = obj["RequiresUM"]
      """  For most Intrastat commodity codes, the UM (or "Supplementary Unit") does not need to be reported. A TRUE value for this field, indicates that a secondary quantity is needed for Intrastat reporting.  """  
      self.NotReported:bool = obj["NotReported"]
      """  Indicates if the commodity code does not need to be reported on Intrastat reports.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StatImportCode:str = obj["StatImportCode"]
      """  Optional field to store the Statistical Import Code.  For reporting purposes only.  """  
      self.StatExportCode:str = obj["StatExportCode"]
      """  Optional field to store the Statistical Export Code.  For reporting purposes only.  """  
      self.ImportCode:str = obj["ImportCode"]
      """  Optional field to store the Import Code.  For reporting purposes only.  """  
      self.ExportCode:str = obj["ExportCode"]
      """  Optional field to store the Export Code.  For reporting purposes only.  """  
      self.GlobalICommCode:bool = obj["GlobalICommCode"]
      """  Marks this ICommCode as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Intrastat:bool = obj["Intrastat"]
      """  True if Intrastat is enabled in company  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ICommCodeListTableset:
   def __init__(self, obj):
      self.ICommCodeList:list[Erp_Tablesets_ICommCodeListRow] = obj["ICommCodeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ICommCodeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.Description:str = obj["Description"]
      """  Full description of the Commodity Code.  """  
      self.RequiresWeight:bool = obj["RequiresWeight"]
      """  For most Intrastat commodity codes, the weight does not need to be reported. A TRUE value for this field, indicates that the weight is needed for Intrastat reporting. Posting of invoices may be blocked (ISSyst.BlockWeight) if there exists a line with a required weight equal to zero.  """  
      self.RequiresUM:bool = obj["RequiresUM"]
      """  For most Intrastat commodity codes, the UM (or "Supplementary Unit") does not need to be reported. A TRUE value for this field, indicates that a secondary quantity is needed for Intrastat reporting.  """  
      self.NotReported:bool = obj["NotReported"]
      """  Indicates if the commodity code does not need to be reported on Intrastat reports.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StatImportCode:str = obj["StatImportCode"]
      """  Optional field to store the Statistical Import Code.  For reporting purposes only.  """  
      self.StatExportCode:str = obj["StatExportCode"]
      """  Optional field to store the Statistical Export Code.  For reporting purposes only.  """  
      self.ImportCode:str = obj["ImportCode"]
      """  Optional field to store the Import Code.  For reporting purposes only.  """  
      self.ExportCode:str = obj["ExportCode"]
      """  Optional field to store the Export Code.  For reporting purposes only.  """  
      self.GlobalICommCode:bool = obj["GlobalICommCode"]
      """  Marks this ICommCode as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SuppUnitsUOM:str = obj["SuppUnitsUOM"]
      """  SuppUnitsUOM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCustomsTaxRate:int = obj["CNCustomsTaxRate"]
      """  Customs Duty Rate  """  
      self.CNDescription:str = obj["CNDescription"]
      """  CN Description  """  
      self.TaricCode:str = obj["TaricCode"]
      """  European Union integrated tariff.  """  
      self.EUPreference:str = obj["EUPreference"]
      """  European Union preference.  """  
      self.Intrastat:bool = obj["Intrastat"]
      """  True if Intrastat is enabled in company  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ICommCodeTableset:
   def __init__(self, obj):
      self.ICommCode:list[Erp_Tablesets_ICommCodeRow] = obj["ICommCode"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtICommCodeTableset:
   def __init__(self, obj):
      self.ICommCode:list[Erp_Tablesets_ICommCodeRow] = obj["ICommCode"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   commodityCode
   """  
   def __init__(self, obj):
      self.commodityCode:str = obj["commodityCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ICommCodeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ICommCodeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ICommCodeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ICommCodeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewICommCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ICommCodeTableset] = obj["ds"]
      pass

class GetNewICommCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ICommCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseICommCode
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseICommCode:str = obj["whereClauseICommCode"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ICommCodeTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtICommCodeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtICommCodeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ICommCodeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ICommCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

