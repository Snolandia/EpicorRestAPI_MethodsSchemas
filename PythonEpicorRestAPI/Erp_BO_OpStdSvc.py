import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.OpStdSvc
# Description: Operation Standards Master.
This file is maintained from within WorkCenter or Operation master maintenance programs.
DELETE: Not allowed if referenced in JobOper, or BomOper
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_OpStds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpStds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpStds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpStdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/OpStds",headers=creds) as resp:
           return await resp.json()

async def post_OpStds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpStds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpStdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpStdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/OpStds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpStds_Company_ResourceGrpID_OpCode_OpStdID(Company, ResourceGrpID, OpCode, OpStdID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpStd item
   Description: Calls GetByID to retrieve the OpStd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpStd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param OpStdID: Desc: OpStdID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpStdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/OpStds(" + Company + "," + ResourceGrpID + "," + OpCode + "," + OpStdID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpStds_Company_ResourceGrpID_OpCode_OpStdID(Company, ResourceGrpID, OpCode, OpStdID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpStd for the service
   Description: Calls UpdateExt to update OpStd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpStd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param OpStdID: Desc: OpStdID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpStdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/OpStds(" + Company + "," + ResourceGrpID + "," + OpCode + "," + OpStdID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpStds_Company_ResourceGrpID_OpCode_OpStdID(Company, ResourceGrpID, OpCode, OpStdID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpStd item
   Description: Call UpdateExt to delete OpStd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpStd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param OpStdID: Desc: OpStdID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/OpStds(" + Company + "," + ResourceGrpID + "," + OpCode + "," + OpStdID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpStdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseOpStd, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseOpStd=" + whereClauseOpStd
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(resourceGrpID, opCode, opStdID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "resourceGrpID=" + resourceGrpID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "opCode=" + opCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "opStdID=" + opStdID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpStd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpStd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpStd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpStd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpStd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpStdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpStdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpStdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpStdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpStdRow] = obj["value"]
      pass

class Erp_Tablesets_OpStdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Code of Resource Group that this standard is related to.  Must be valid in the ResourceGrp file.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master ID that this standard is related to. Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """  A descriptive ID used to identify the standard within the workcenter/operation.  """  
      self.Description:str = obj["Description"]
      """  Description of the operation standard.  Cannot be blank.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.  Job entry uses this X SetupCrewSize to get a default for SetupLaborHrs.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """  Std can be configured as Hours, Minutes per Piece, Pieces per Time, Operations per Minute or Operations per hour.  This is used as a default in the actual operation detail records that reference this standard.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute "HR" - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a divisor. Valid codes are U-Units, C=100's, M=1000's, T=10,000.
If user has a standard based on how long it takes to do 1000 pieces and an operation takes 2 hours. It would be filled in as Prod standard of "2.00", Qualifier of "HP", and Basis of "M"  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description  """  
      self.WCName:str = obj["WCName"]
      """  WorkCenter Name  """  
      self.SetupGroupDesc:str = obj["SetupGroupDesc"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      """  Description of Setup Group.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpStdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Code of Resource Group that this standard is related to.  Must be valid in the ResourceGrp file.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master ID that this standard is related to. Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """  A descriptive ID used to identify the standard within the workcenter/operation.  """  
      self.Description:str = obj["Description"]
      """  Description of the operation standard.  Cannot be blank.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.  Job entry uses this X SetupCrewSize to get a default for SetupLaborHrs.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """  Std can be configured as Hours, Minutes per Piece, Pieces per Time, Operations per Minute or Operations per hour.  This is used as a default in the actual operation detail records that reference this standard.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute "HR" - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a divisor. Valid codes are U-Units, C=100's, M=1000's, T=10,000.
If user has a standard based on how long it takes to do 1000 pieces and an operation takes 2 hours. It would be filled in as Prod standard of "2.00", Qualifier of "HP", and Basis of "M"  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description  """  
      self.SetupGroupDesc:str = obj["SetupGroupDesc"]
      self.WCName:str = obj["WCName"]
      """  WorkCenter Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   resourceGrpID
   opCode
   opStdID
   """  
   def __init__(self, obj):
      self.resourceGrpID:str = obj["resourceGrpID"]
      self.opCode:str = obj["opCode"]
      self.opStdID:str = obj["opStdID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_OpStdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Code of Resource Group that this standard is related to.  Must be valid in the ResourceGrp file.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master ID that this standard is related to. Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """  A descriptive ID used to identify the standard within the workcenter/operation.  """  
      self.Description:str = obj["Description"]
      """  Description of the operation standard.  Cannot be blank.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.  Job entry uses this X SetupCrewSize to get a default for SetupLaborHrs.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """  Std can be configured as Hours, Minutes per Piece, Pieces per Time, Operations per Minute or Operations per hour.  This is used as a default in the actual operation detail records that reference this standard.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute "HR" - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a divisor. Valid codes are U-Units, C=100's, M=1000's, T=10,000.
If user has a standard based on how long it takes to do 1000 pieces and an operation takes 2 hours. It would be filled in as Prod standard of "2.00", Qualifier of "HP", and Basis of "M"  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description  """  
      self.WCName:str = obj["WCName"]
      """  WorkCenter Name  """  
      self.SetupGroupDesc:str = obj["SetupGroupDesc"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      """  Description of Setup Group.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpStdListTableset:
   def __init__(self, obj):
      self.OpStdList:list[Erp_Tablesets_OpStdListRow] = obj["OpStdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_OpStdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Code of Resource Group that this standard is related to.  Must be valid in the ResourceGrp file.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master ID that this standard is related to. Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """  A descriptive ID used to identify the standard within the workcenter/operation.  """  
      self.Description:str = obj["Description"]
      """  Description of the operation standard.  Cannot be blank.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.  Job entry uses this X SetupCrewSize to get a default for SetupLaborHrs.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """  Std can be configured as Hours, Minutes per Piece, Pieces per Time, Operations per Minute or Operations per hour.  This is used as a default in the actual operation detail records that reference this standard.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute "HR" - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a divisor. Valid codes are U-Units, C=100's, M=1000's, T=10,000.
If user has a standard based on how long it takes to do 1000 pieces and an operation takes 2 hours. It would be filled in as Prod standard of "2.00", Qualifier of "HP", and Basis of "M"  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description  """  
      self.SetupGroupDesc:str = obj["SetupGroupDesc"]
      self.WCName:str = obj["WCName"]
      """  WorkCenter Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpStdTableset:
   def __init__(self, obj):
      self.OpStd:list[Erp_Tablesets_OpStdRow] = obj["OpStd"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtOpStdTableset:
   def __init__(self, obj):
      self.OpStd:list[Erp_Tablesets_OpStdRow] = obj["OpStd"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   resourceGrpID
   opCode
   opStdID
   """  
   def __init__(self, obj):
      self.resourceGrpID:str = obj["resourceGrpID"]
      self.opCode:str = obj["opCode"]
      self.opStdID:str = obj["opStdID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpStdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OpStdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OpStdTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OpStdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewOpStd_input:
   """ Required : 
   ds
   resourceGrpID
   opCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpStdTableset] = obj["ds"]
      self.resourceGrpID:str = obj["resourceGrpID"]
      self.opCode:str = obj["opCode"]
      pass

class GetNewOpStd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpStdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseOpStd
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOpStd:str = obj["whereClauseOpStd"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpStdTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtOpStdTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtOpStdTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpStdTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpStdTableset] = obj["ds"]
      pass

      """  output parameters  """  

