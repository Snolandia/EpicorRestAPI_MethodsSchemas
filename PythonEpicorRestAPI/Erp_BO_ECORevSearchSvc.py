import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ECORevSearchSvc
# Description: ECO Rev Search module
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ECORevSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECORevSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECORevSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches",headers=creds) as resp:
           return await resp.json()

async def post_ECORevSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECORevSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECORevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECORevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECORevSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECORevSearch item
   Description: Calls GetByID to retrieve the ECORevSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORevSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECORevSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECORevSearch for the service
   Description: Calls UpdateExt to update ECORevSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECORevSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECORevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECORevSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECORevSearch item
   Description: Call UpdateExt to delete ECORevSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECORevSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseECORev, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseECORev=" + whereClauseECORev
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, partNum, revisionNum, altMethod, processMfgID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "revisionNum=" + revisionNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "altMethod=" + altMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "processMfgID=" + processMfgID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECORev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECORev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECORevListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECORevRow] = obj["value"]
      pass

class Erp_Tablesets_ECORevListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.CheckInRevisionNum:str = obj["CheckInRevisionNum"]
      """  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  """  
      self.CheckInDate:str = obj["CheckInDate"]
      """  The date that the revision is checked in.  """  
      self.CheckedOut:bool = obj["CheckedOut"]
      """  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  """  
      self.CheckOutDate:str = obj["CheckOutDate"]
      """  The date that the Part-Rev was last checked out to the group.  """  
      self.CheckedOutBy:str = obj["CheckedOutBy"]
      """  UserID who checked out the revision.  Not maintainable by the user.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.RevLocked:bool = obj["RevLocked"]
      """  Indicates if this ECO Revision is locked.  """  
      self.RevLockedBy:str = obj["RevLockedBy"]
      """  UserID that has the ECORev record locked.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  AltMethodDesc  """  
      self.IsPartRev:bool = obj["IsPartRev"]
      """  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  """  
      self.EnableLock:bool = obj["EnableLock"]
      """  Should the Lock menu option be enabled?  """  
      self.EnableUnLock:bool = obj["EnableUnLock"]
      """  Should the UnLock menu option be enabled?  """  
      self.EnableUpdateable:bool = obj["EnableUpdateable"]
      """  Is the revision updateable?  Used for menu options.  """  
      self.EnableGetDetails:bool = obj["EnableGetDetails"]
      """  Should the GetDetails menu options be enabled?  """  
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      """  The text description of the ECO Group  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECORevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.CheckInRevisionNum:str = obj["CheckInRevisionNum"]
      """  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  """  
      self.CheckInDate:str = obj["CheckInDate"]
      """  The date that the revision is checked in.  """  
      self.CheckedOut:bool = obj["CheckedOut"]
      """  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  """  
      self.CheckOutDate:str = obj["CheckOutDate"]
      """  The date that the Part-Rev was last checked out to the group.  """  
      self.CheckedOutBy:str = obj["CheckedOutBy"]
      """  UserID who checked out the revision.  Not maintainable by the user.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.RevLocked:bool = obj["RevLocked"]
      """  Indicates if this ECO Revision is locked.  """  
      self.RevLockedBy:str = obj["RevLockedBy"]
      """  UserID that has the ECORev record locked.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Identifies whether the co-parts are to be produced concurrently or sequentially. The default is sequential. The selected value determines quantity reporting and costing.  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  AltMethodDesc  """  
      self.CNCustomsItemNum:str = obj["CNCustomsItemNum"]
      """  Customs Item Number  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: Cleaning, General, Master and Site.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.ImageID:str = obj["ImageID"]
      """  ID of Revision Image.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.Configured:bool = obj["Configured"]
      self.EnableGetDetails:bool = obj["EnableGetDetails"]
      """  Should the GetDetails menu options be enabled?  """  
      self.EnableUnLock:bool = obj["EnableUnLock"]
      """  Should the UnLock menu option be enabled?  """  
      self.EnableUpdateable:bool = obj["EnableUpdateable"]
      """  Is the revision updateable?  Used for menu options.  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      self.IsPartRev:bool = obj["IsPartRev"]
      """  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  """  
      self.EnableLock:bool = obj["EnableLock"]
      """  Should the Lock menu option be enabled?  """  
      self.CNHandbookLine:str = obj["CNHandbookLine"]
      """  Handbook Line  """  
      self.CNHandbookCode:str = obj["CNHandbookCode"]
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      self.isFromPartRevision:bool = obj["isFromPartRevision"]
      self.AltMethodDisplay:str = obj["AltMethodDisplay"]
      """  AltMethod string with label for kinetic tree binding in EngWorkBenchEntry  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTypeCode:str = obj["PartNumTypeCode"]
      self.PartRevCreatedBy:str = obj["PartRevCreatedBy"]
      self.PartRevCreatedOn:str = obj["PartRevCreatedOn"]
      self.PartRevApproved:bool = obj["PartRevApproved"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ECORevListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.CheckInRevisionNum:str = obj["CheckInRevisionNum"]
      """  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  """  
      self.CheckInDate:str = obj["CheckInDate"]
      """  The date that the revision is checked in.  """  
      self.CheckedOut:bool = obj["CheckedOut"]
      """  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  """  
      self.CheckOutDate:str = obj["CheckOutDate"]
      """  The date that the Part-Rev was last checked out to the group.  """  
      self.CheckedOutBy:str = obj["CheckedOutBy"]
      """  UserID who checked out the revision.  Not maintainable by the user.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.RevLocked:bool = obj["RevLocked"]
      """  Indicates if this ECO Revision is locked.  """  
      self.RevLockedBy:str = obj["RevLockedBy"]
      """  UserID that has the ECORev record locked.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  AltMethodDesc  """  
      self.IsPartRev:bool = obj["IsPartRev"]
      """  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  """  
      self.EnableLock:bool = obj["EnableLock"]
      """  Should the Lock menu option be enabled?  """  
      self.EnableUnLock:bool = obj["EnableUnLock"]
      """  Should the UnLock menu option be enabled?  """  
      self.EnableUpdateable:bool = obj["EnableUpdateable"]
      """  Is the revision updateable?  Used for menu options.  """  
      self.EnableGetDetails:bool = obj["EnableGetDetails"]
      """  Should the GetDetails menu options be enabled?  """  
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      """  The text description of the ECO Group  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECORevListTableset:
   def __init__(self, obj):
      self.ECORevList:list[Erp_Tablesets_ECORevListRow] = obj["ECORevList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ECORevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.CheckInRevisionNum:str = obj["CheckInRevisionNum"]
      """  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  """  
      self.CheckInDate:str = obj["CheckInDate"]
      """  The date that the revision is checked in.  """  
      self.CheckedOut:bool = obj["CheckedOut"]
      """  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  """  
      self.CheckOutDate:str = obj["CheckOutDate"]
      """  The date that the Part-Rev was last checked out to the group.  """  
      self.CheckedOutBy:str = obj["CheckedOutBy"]
      """  UserID who checked out the revision.  Not maintainable by the user.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.RevLocked:bool = obj["RevLocked"]
      """  Indicates if this ECO Revision is locked.  """  
      self.RevLockedBy:str = obj["RevLockedBy"]
      """  UserID that has the ECORev record locked.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Identifies whether the co-parts are to be produced concurrently or sequentially. The default is sequential. The selected value determines quantity reporting and costing.  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  AltMethodDesc  """  
      self.CNCustomsItemNum:str = obj["CNCustomsItemNum"]
      """  Customs Item Number  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: Cleaning, General, Master and Site.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.ImageID:str = obj["ImageID"]
      """  ID of Revision Image.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.Configured:bool = obj["Configured"]
      self.EnableGetDetails:bool = obj["EnableGetDetails"]
      """  Should the GetDetails menu options be enabled?  """  
      self.EnableUnLock:bool = obj["EnableUnLock"]
      """  Should the UnLock menu option be enabled?  """  
      self.EnableUpdateable:bool = obj["EnableUpdateable"]
      """  Is the revision updateable?  Used for menu options.  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      self.IsPartRev:bool = obj["IsPartRev"]
      """  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  """  
      self.EnableLock:bool = obj["EnableLock"]
      """  Should the Lock menu option be enabled?  """  
      self.CNHandbookLine:str = obj["CNHandbookLine"]
      """  Handbook Line  """  
      self.CNHandbookCode:str = obj["CNHandbookCode"]
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      self.isFromPartRevision:bool = obj["isFromPartRevision"]
      self.AltMethodDisplay:str = obj["AltMethodDisplay"]
      """  AltMethod string with label for kinetic tree binding in EngWorkBenchEntry  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTypeCode:str = obj["PartNumTypeCode"]
      self.PartRevCreatedBy:str = obj["PartRevCreatedBy"]
      self.PartRevCreatedOn:str = obj["PartRevCreatedOn"]
      self.PartRevApproved:bool = obj["PartRevApproved"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECORevSearchTableset:
   def __init__(self, obj):
      self.ECORev:list[Erp_Tablesets_ECORevRow] = obj["ECORev"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtECORevSearchTableset:
   def __init__(self, obj):
      self.ECORev:list[Erp_Tablesets_ECORevRow] = obj["ECORev"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECORevSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECORevSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECORevSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECORevListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewECORev_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECORevSearchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      pass

class GetNewECORev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECORevSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseECORev
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseECORev:str = obj["whereClauseECORev"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECORevSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtECORevSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtECORevSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECORevSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECORevSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

