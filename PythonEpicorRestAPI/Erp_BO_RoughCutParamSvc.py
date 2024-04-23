import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RoughCutParamSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RoughCutParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RoughCutParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RoughCutParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RoughCutParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/RoughCutParams",headers=creds) as resp:
           return await resp.json()

async def post_RoughCutParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RoughCutParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RoughCutParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RoughCutParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/RoughCutParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RoughCutParams_Company_RoughCutCode(Company, RoughCutCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RoughCutParam item
   Description: Calls GetByID to retrieve the RoughCutParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RoughCutParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoughCutCode: Desc: RoughCutCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RoughCutParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/RoughCutParams(" + Company + "," + RoughCutCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RoughCutParams_Company_RoughCutCode(Company, RoughCutCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RoughCutParam for the service
   Description: Calls UpdateExt to update RoughCutParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RoughCutParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoughCutCode: Desc: RoughCutCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RoughCutParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/RoughCutParams(" + Company + "," + RoughCutCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RoughCutParams_Company_RoughCutCode(Company, RoughCutCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RoughCutParam item
   Description: Call UpdateExt to delete RoughCutParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RoughCutParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoughCutCode: Desc: RoughCutCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/RoughCutParams(" + Company + "," + RoughCutCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RoughCutParamListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRoughCutParam, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRoughCutParam=" + whereClauseRoughCutParam
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(roughCutCode, epicorHeaders = None):
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
   params += "roughCutCode=" + roughCutCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRoughCutParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRoughCutParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRoughCutParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRoughCutParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRoughCutParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoughCutParamSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoughCutParamListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RoughCutParamListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoughCutParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RoughCutParamRow] = obj["value"]
      pass

class Erp_Tablesets_RoughCutParamListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Unique identifier for a set of rough cut schedule parameters.  """  
      self.Description:str = obj["Description"]
      """  Full description of the rough cut parameter set.  """  
      self.SetupPct:int = obj["SetupPct"]
      """  Percentage that setup hours will be increased when rough cut scheduling.  """  
      self.SetupMinChgHrs:int = obj["SetupMinChgHrs"]
      """  Minimum threshold of change.  Calculated setup hours not meeting the minimum will be adjusted to the minimum.  """  
      self.SetupMaxChgHrs:int = obj["SetupMaxChgHrs"]
      """  Maximum threshold of change.  Calculated setup hours exceeding the maximum will be adjusted to the maximum.  """  
      self.FixedPct:int = obj["FixedPct"]
      """  Percentage that fixed hours will be increased when rough cut scheduling.  """  
      self.FixedMinChgHrs:int = obj["FixedMinChgHrs"]
      """  Minimum threshold of change.  Calculated fixed hours not meeting the minimum will be adjusted to the minimum.  """  
      self.FixedMaxChgHrs:int = obj["FixedMaxChgHrs"]
      """  Maximum threshold of change.  Calculated fixed hours exceeding the maximum will be adjusted to the maximum.  """  
      self.VariablePct:int = obj["VariablePct"]
      """  Percentage that variable hours will be increased when rough cut scheduling.  """  
      self.VarMinChgHrs:int = obj["VarMinChgHrs"]
      """  Minimum threshold of change.  Calculated variable hours not meeting the minimum will be adjusted to the minimum.  """  
      self.VarMaxChgHrs:int = obj["VarMaxChgHrs"]
      """  Maximum threshold of change.  Calculated variable hours exceeding the maximum will be adjusted to the maximum.  """  
      self.SubCntPct:int = obj["SubCntPct"]
      """  Percentage that subcontract days out will be increased when rough cut scheduling.  """  
      self.SubCMinChgDays:int = obj["SubCMinChgDays"]
      """  Minimum threshold of change.  Calculated subcontract days out not meeting the minimum will be adjusted to the minimum.  """  
      self.SubCMaxChgDays:int = obj["SubCMaxChgDays"]
      """  Maximum threshold of change.  Calculated subcontract days out exceeding the maximum will be adjusted to the maximum.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RoughCutParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Unique identifier for a set of rough cut schedule parameters.  """  
      self.Description:str = obj["Description"]
      """  Full description of the rough cut parameter set.  """  
      self.SetupPct:int = obj["SetupPct"]
      """  Percentage that setup hours will be increased when rough cut scheduling.  """  
      self.SetupMinChgHrs:int = obj["SetupMinChgHrs"]
      """  Minimum threshold of change.  Calculated setup hours not meeting the minimum will be adjusted to the minimum.  """  
      self.SetupMaxChgHrs:int = obj["SetupMaxChgHrs"]
      """  Maximum threshold of change.  Calculated setup hours exceeding the maximum will be adjusted to the maximum.  """  
      self.FixedPct:int = obj["FixedPct"]
      """  Percentage that fixed hours will be increased when rough cut scheduling.  """  
      self.FixedMinChgHrs:int = obj["FixedMinChgHrs"]
      """  Minimum threshold of change.  Calculated fixed hours not meeting the minimum will be adjusted to the minimum.  """  
      self.FixedMaxChgHrs:int = obj["FixedMaxChgHrs"]
      """  Maximum threshold of change.  Calculated fixed hours exceeding the maximum will be adjusted to the maximum.  """  
      self.VariablePct:int = obj["VariablePct"]
      """  Percentage that variable hours will be increased when rough cut scheduling.  """  
      self.VarMinChgHrs:int = obj["VarMinChgHrs"]
      """  Minimum threshold of change.  Calculated variable hours not meeting the minimum will be adjusted to the minimum.  """  
      self.VarMaxChgHrs:int = obj["VarMaxChgHrs"]
      """  Maximum threshold of change.  Calculated variable hours exceeding the maximum will be adjusted to the maximum.  """  
      self.SubCntPct:int = obj["SubCntPct"]
      """  Percentage that subcontract days out will be increased when rough cut scheduling.  """  
      self.SubCMinChgDays:int = obj["SubCMinChgDays"]
      """  Minimum threshold of change.  Calculated subcontract days out not meeting the minimum will be adjusted to the minimum.  """  
      self.SubCMaxChgDays:int = obj["SubCMaxChgDays"]
      """  Maximum threshold of change.  Calculated subcontract days out exceeding the maximum will be adjusted to the maximum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   roughCutCode
   """  
   def __init__(self, obj):
      self.roughCutCode:str = obj["roughCutCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_RoughCutParamListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Unique identifier for a set of rough cut schedule parameters.  """  
      self.Description:str = obj["Description"]
      """  Full description of the rough cut parameter set.  """  
      self.SetupPct:int = obj["SetupPct"]
      """  Percentage that setup hours will be increased when rough cut scheduling.  """  
      self.SetupMinChgHrs:int = obj["SetupMinChgHrs"]
      """  Minimum threshold of change.  Calculated setup hours not meeting the minimum will be adjusted to the minimum.  """  
      self.SetupMaxChgHrs:int = obj["SetupMaxChgHrs"]
      """  Maximum threshold of change.  Calculated setup hours exceeding the maximum will be adjusted to the maximum.  """  
      self.FixedPct:int = obj["FixedPct"]
      """  Percentage that fixed hours will be increased when rough cut scheduling.  """  
      self.FixedMinChgHrs:int = obj["FixedMinChgHrs"]
      """  Minimum threshold of change.  Calculated fixed hours not meeting the minimum will be adjusted to the minimum.  """  
      self.FixedMaxChgHrs:int = obj["FixedMaxChgHrs"]
      """  Maximum threshold of change.  Calculated fixed hours exceeding the maximum will be adjusted to the maximum.  """  
      self.VariablePct:int = obj["VariablePct"]
      """  Percentage that variable hours will be increased when rough cut scheduling.  """  
      self.VarMinChgHrs:int = obj["VarMinChgHrs"]
      """  Minimum threshold of change.  Calculated variable hours not meeting the minimum will be adjusted to the minimum.  """  
      self.VarMaxChgHrs:int = obj["VarMaxChgHrs"]
      """  Maximum threshold of change.  Calculated variable hours exceeding the maximum will be adjusted to the maximum.  """  
      self.SubCntPct:int = obj["SubCntPct"]
      """  Percentage that subcontract days out will be increased when rough cut scheduling.  """  
      self.SubCMinChgDays:int = obj["SubCMinChgDays"]
      """  Minimum threshold of change.  Calculated subcontract days out not meeting the minimum will be adjusted to the minimum.  """  
      self.SubCMaxChgDays:int = obj["SubCMaxChgDays"]
      """  Maximum threshold of change.  Calculated subcontract days out exceeding the maximum will be adjusted to the maximum.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RoughCutParamListTableset:
   def __init__(self, obj):
      self.RoughCutParamList:list[Erp_Tablesets_RoughCutParamListRow] = obj["RoughCutParamList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RoughCutParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Unique identifier for a set of rough cut schedule parameters.  """  
      self.Description:str = obj["Description"]
      """  Full description of the rough cut parameter set.  """  
      self.SetupPct:int = obj["SetupPct"]
      """  Percentage that setup hours will be increased when rough cut scheduling.  """  
      self.SetupMinChgHrs:int = obj["SetupMinChgHrs"]
      """  Minimum threshold of change.  Calculated setup hours not meeting the minimum will be adjusted to the minimum.  """  
      self.SetupMaxChgHrs:int = obj["SetupMaxChgHrs"]
      """  Maximum threshold of change.  Calculated setup hours exceeding the maximum will be adjusted to the maximum.  """  
      self.FixedPct:int = obj["FixedPct"]
      """  Percentage that fixed hours will be increased when rough cut scheduling.  """  
      self.FixedMinChgHrs:int = obj["FixedMinChgHrs"]
      """  Minimum threshold of change.  Calculated fixed hours not meeting the minimum will be adjusted to the minimum.  """  
      self.FixedMaxChgHrs:int = obj["FixedMaxChgHrs"]
      """  Maximum threshold of change.  Calculated fixed hours exceeding the maximum will be adjusted to the maximum.  """  
      self.VariablePct:int = obj["VariablePct"]
      """  Percentage that variable hours will be increased when rough cut scheduling.  """  
      self.VarMinChgHrs:int = obj["VarMinChgHrs"]
      """  Minimum threshold of change.  Calculated variable hours not meeting the minimum will be adjusted to the minimum.  """  
      self.VarMaxChgHrs:int = obj["VarMaxChgHrs"]
      """  Maximum threshold of change.  Calculated variable hours exceeding the maximum will be adjusted to the maximum.  """  
      self.SubCntPct:int = obj["SubCntPct"]
      """  Percentage that subcontract days out will be increased when rough cut scheduling.  """  
      self.SubCMinChgDays:int = obj["SubCMinChgDays"]
      """  Minimum threshold of change.  Calculated subcontract days out not meeting the minimum will be adjusted to the minimum.  """  
      self.SubCMaxChgDays:int = obj["SubCMaxChgDays"]
      """  Maximum threshold of change.  Calculated subcontract days out exceeding the maximum will be adjusted to the maximum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RoughCutParamTableset:
   def __init__(self, obj):
      self.RoughCutParam:list[Erp_Tablesets_RoughCutParamRow] = obj["RoughCutParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRoughCutParamTableset:
   def __init__(self, obj):
      self.RoughCutParam:list[Erp_Tablesets_RoughCutParamRow] = obj["RoughCutParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   roughCutCode
   """  
   def __init__(self, obj):
      self.roughCutCode:str = obj["roughCutCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RoughCutParamTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RoughCutParamTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RoughCutParamTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RoughCutParamListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRoughCutParam_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RoughCutParamTableset] = obj["ds"]
      pass

class GetNewRoughCutParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RoughCutParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRoughCutParam
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRoughCutParam:str = obj["whereClauseRoughCutParam"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RoughCutParamTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtRoughCutParamTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRoughCutParamTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RoughCutParamTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RoughCutParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

