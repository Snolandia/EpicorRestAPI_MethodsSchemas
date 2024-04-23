import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CostPartSearchSvc
# Description: Cost Part Search
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CostPartSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CostPartSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostPartSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches",headers=creds) as resp:
           return await resp.json()

async def post_CostPartSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostPartSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CostPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CostPartSearches_Company_GroupID_TypeCode_PartNum(Company, GroupID, TypeCode, PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CostPartSearch item
   Description: Calls GetByID to retrieve the CostPartSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostPartSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CostPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CostPartSearches_Company_GroupID_TypeCode_PartNum(Company, GroupID, TypeCode, PartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CostPartSearch for the service
   Description: Calls UpdateExt to update CostPartSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostPartSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CostPartSearches_Company_GroupID_TypeCode_PartNum(Company, GroupID, TypeCode, PartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CostPartSearch item
   Description: Call UpdateExt to delete CostPartSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostPartSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostPartListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCostPart, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCostPart=" + whereClauseCostPart
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, typeCode, partNum, epicorHeaders = None):
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
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "typeCode=" + typeCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCostPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCostPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCostPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CostPartListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CostPartRow] = obj["value"]
      pass

class Erp_Tablesets_CostPartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """   Standard Burden Unit Cost.

( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """   Standard Material Unit cost.

( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  """  
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
      """  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      self.IsMethod:bool = obj["IsMethod"]
      self.ApprovedMethod:bool = obj["ApprovedMethod"]
      self.CurrentRevisionNum:str = obj["CurrentRevisionNum"]
      self.CurrentRevDescription:str = obj["CurrentRevDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      """  Description  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      """  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.TypeCodeTypeDescription:str = obj["TypeCodeTypeDescription"]
      """  Full Description of the Type of task.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """   Standard Burden Unit Cost.

( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """   Standard Material Unit cost.

( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  """  
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
      """  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimCostPart:str = obj["PrimCostPart"]
      """  PrimCostPart  """  
      self.PrimCostRev:str = obj["PrimCostRev"]
      """  PrimCostRev  """  
      self.PrimCostAltMethod:str = obj["PrimCostAltMethod"]
      """  PrimCostAltMethod  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  CoPartsReqQty  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  MtlCostPct  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  LaborCostPct  """  
      self.OrigStdMaterialCost:int = obj["OrigStdMaterialCost"]
      """  OrigStdMaterialCost  """  
      self.OrigStdLaborCost:int = obj["OrigStdLaborCost"]
      """  OrigStdLaborCost  """  
      self.OrigStdBurdenCost:int = obj["OrigStdBurdenCost"]
      """  OrigStdBurdenCost  """  
      self.OrigStdSubContCost:int = obj["OrigStdSubContCost"]
      """  OrigStdSubContCost  """  
      self.OrigStdMtlBurCost:int = obj["OrigStdMtlBurCost"]
      """  OrigStdMtlBurCost  """  
      self.IsTransferCostID:bool = obj["IsTransferCostID"]
      """  IsTransferCostID  """  
      self.ApprovedMethod:bool = obj["ApprovedMethod"]
      self.CurrentRevDescription:str = obj["CurrentRevDescription"]
      self.CurrentRevisionNum:str = obj["CurrentRevisionNum"]
      self.IsMethod:bool = obj["IsMethod"]
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.TypeCodeTypeDescription:str = obj["TypeCodeTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   groupID
   typeCode
   partNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.typeCode:str = obj["typeCode"]
      self.partNum:str = obj["partNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CostPartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """   Standard Burden Unit Cost.

( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """   Standard Material Unit cost.

( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  """  
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
      """  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      self.IsMethod:bool = obj["IsMethod"]
      self.ApprovedMethod:bool = obj["ApprovedMethod"]
      self.CurrentRevisionNum:str = obj["CurrentRevisionNum"]
      self.CurrentRevDescription:str = obj["CurrentRevDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      """  Description  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      """  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.TypeCodeTypeDescription:str = obj["TypeCodeTypeDescription"]
      """  Full Description of the Type of task.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostPartListTableset:
   def __init__(self, obj):
      self.CostPartList:list[Erp_Tablesets_CostPartListRow] = obj["CostPartList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """   Standard Burden Unit Cost.

( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """   Standard Material Unit cost.

( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  """  
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
      """  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision.  """  
      self.Linked:bool = obj["Linked"]
      """  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimCostPart:str = obj["PrimCostPart"]
      """  PrimCostPart  """  
      self.PrimCostRev:str = obj["PrimCostRev"]
      """  PrimCostRev  """  
      self.PrimCostAltMethod:str = obj["PrimCostAltMethod"]
      """  PrimCostAltMethod  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  CoPartsReqQty  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  MtlCostPct  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  LaborCostPct  """  
      self.OrigStdMaterialCost:int = obj["OrigStdMaterialCost"]
      """  OrigStdMaterialCost  """  
      self.OrigStdLaborCost:int = obj["OrigStdLaborCost"]
      """  OrigStdLaborCost  """  
      self.OrigStdBurdenCost:int = obj["OrigStdBurdenCost"]
      """  OrigStdBurdenCost  """  
      self.OrigStdSubContCost:int = obj["OrigStdSubContCost"]
      """  OrigStdSubContCost  """  
      self.OrigStdMtlBurCost:int = obj["OrigStdMtlBurCost"]
      """  OrigStdMtlBurCost  """  
      self.IsTransferCostID:bool = obj["IsTransferCostID"]
      """  IsTransferCostID  """  
      self.ApprovedMethod:bool = obj["ApprovedMethod"]
      self.CurrentRevDescription:str = obj["CurrentRevDescription"]
      self.CurrentRevisionNum:str = obj["CurrentRevisionNum"]
      self.IsMethod:bool = obj["IsMethod"]
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.TypeCodeTypeDescription:str = obj["TypeCodeTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostPartSearchTableset:
   def __init__(self, obj):
      self.CostPart:list[Erp_Tablesets_CostPartRow] = obj["CostPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCostPartSearchTableset:
   def __init__(self, obj):
      self.CostPart:list[Erp_Tablesets_CostPartRow] = obj["CostPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   typeCode
   partNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.typeCode:str = obj["typeCode"]
      self.partNum:str = obj["partNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostPartSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CostPartSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CostPartSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CostPartListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCostPart_input:
   """ Required : 
   ds
   groupID
   typeCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostPartSearchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.typeCode:str = obj["typeCode"]
      pass

class GetNewCostPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostPartSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCostPart
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCostPart:str = obj["whereClauseCostPart"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostPartSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCostPartSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCostPartSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostPartSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostPartSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

