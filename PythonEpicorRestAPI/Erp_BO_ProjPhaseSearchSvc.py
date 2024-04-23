import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ProjPhaseSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ProjPhaseSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProjPhaseSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProjPhaseSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjPhaseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches",headers=creds) as resp:
           return await resp.json()

async def post_ProjPhaseSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProjPhaseSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProjPhaseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProjPhaseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProjPhaseSearches_Company_ProjectID_PhaseID(Company, ProjectID, PhaseID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProjPhaseSearch item
   Description: Calls GetByID to retrieve the ProjPhaseSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProjPhaseSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param PhaseID: Desc: PhaseID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProjPhaseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches(" + Company + "," + ProjectID + "," + PhaseID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProjPhaseSearches_Company_ProjectID_PhaseID(Company, ProjectID, PhaseID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProjPhaseSearch for the service
   Description: Calls UpdateExt to update ProjPhaseSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProjPhaseSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param PhaseID: Desc: PhaseID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProjPhaseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches(" + Company + "," + ProjectID + "," + PhaseID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProjPhaseSearches_Company_ProjectID_PhaseID(Company, ProjectID, PhaseID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProjPhaseSearch item
   Description: Call UpdateExt to delete ProjPhaseSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProjPhaseSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param PhaseID: Desc: PhaseID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches(" + Company + "," + ProjectID + "," + PhaseID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjPhaseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseProjPhase, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseProjPhase=" + whereClauseProjPhase
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(projectID, phaseID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "projectID=" + projectID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "phaseID=" + phaseID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProjPhase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProjPhase
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProjPhase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProjPhase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProjPhase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjPhaseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProjPhaseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjPhaseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProjPhaseRow] = obj["value"]
      pass

class Erp_Tablesets_ProjPhaseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.StartDate:str = obj["StartDate"]
      """  Task start date.  """  
      self.DueDate:str = obj["DueDate"]
      """  Task due date.  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Must be greater than or equal to 0.  """  
      self.DateComplete:str = obj["DateComplete"]
      """  Date this task was complete.  """  
      self.PhaseStatus:str = obj["PhaseStatus"]
      """  Valid values are "N" = Not started, "I" = In Process, "C" = Completed.  """  
      self.Duration:int = obj["Duration"]
      """  This is the duration of the WBS Phase. On the UK software this currently uses field Number09  """  
      self.WBSJobNum:str = obj["WBSJobNum"]
      """  Reference to the job number created for the WBS Phase.  """  
      self.ParentPhase:str = obj["ParentPhase"]
      """  This is the parent phase for this WBS Phase. On the UK software this currently uses field ShortChar01  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back a alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.BudTotBurHrs:int = obj["BudTotBurHrs"]
      """  Total budget burden hours for the Project phase.  """  
      self.BudTotLbrCost:int = obj["BudTotLbrCost"]
      """  Total budget labour cost for the Project phase. This is production and setup combined.  """  
      self.BudTotBurCost:int = obj["BudTotBurCost"]
      """  Total budget burden cost for the Project phase. This is production and setup combined.  """  
      self.BudTotMtlCost:int = obj["BudTotMtlCost"]
      """  Total budget material costs for the Project phase  """  
      self.BudTotMtlBurCost:int = obj["BudTotMtlBurCost"]
      """  Total budget material burden costs for the Project phase.  """  
      self.ManEstCtcLbrHrs:int = obj["ManEstCtcLbrHrs"]
      """  Manually entered estimate to complete for the labour hours for the project phase  """  
      self.ManEstCtcBurHrs:int = obj["ManEstCtcBurHrs"]
      """  Manually entered estimate to complete for the burden hours.  """  
      self.ManEstCtcLbrCost:int = obj["ManEstCtcLbrCost"]
      """  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project phase.  """  
      self.ManEstCtcBurCost:int = obj["ManEstCtcBurCost"]
      """  Manually entered estimate to complete for the burden cost for the project phase.  """  
      self.ManEstCtcSubConCost:int = obj["ManEstCtcSubConCost"]
      """  Manually entered estimate to complete for the Subcontract cost for the project phase.  """  
      self.ManEstCtcMtlCost:int = obj["ManEstCtcMtlCost"]
      """  Manually entered estimate to complete for the material cost for the project phase.  """  
      self.ManEstCtcMtlBurCost:int = obj["ManEstCtcMtlBurCost"]
      """  Manually entered estimate to complete for the material burden cost for the project phase.  """  
      self.TotCtcLbrCost:int = obj["TotCtcLbrCost"]
      """  Total calculated cost to complete labour cost for the Project phase. This will be both production and setup.  """  
      self.TotCtcBurCost:int = obj["TotCtcBurCost"]
      """  Total calculated cost to complete burden cost for the Project phase. This will be both production and setup.  """  
      self.TotCtcSubConCost:int = obj["TotCtcSubConCost"]
      """  Total calculated cost to complete subcontract cost for the Project phase.  """  
      self.TotCtcMtlCost:int = obj["TotCtcMtlCost"]
      """  Total calculated cost to complete material cost for the Project phase.  """  
      self.TotCtcMtlBurCost:int = obj["TotCtcMtlBurCost"]
      """  Total calculated cost to complete material burden cost for the Project phase.  """  
      self.TotQuotLbrHrs:int = obj["TotQuotLbrHrs"]
      """  Total quoted labour hours for the Project phase  """  
      self.TotQuotBurHrs:int = obj["TotQuotBurHrs"]
      """  Total quoted burden hours for the Project phase.  """  
      self.TotQuotLbrCost:int = obj["TotQuotLbrCost"]
      """  Total quoted labour cost for the Project phase. This will be both production and setup.  """  
      self.TotQuotBurCost:int = obj["TotQuotBurCost"]
      """  Total quoted burden cost for the Project phase. This will be both production and setup.  """  
      self.TotQuotSubContCost:int = obj["TotQuotSubContCost"]
      """  Total quoted subcontract cost for the Project phase.  """  
      self.TotQuotMtlCost:int = obj["TotQuotMtlCost"]
      """  Total quoted material cost for the Project phase.  """  
      self.TotQuotMtlBurCost:int = obj["TotQuotMtlBurCost"]
      """  Total quoted material burden cost for the Project phase.  """  
      self.Level:int = obj["Level"]
      """  This holds the bom level of the phase reletive to the parent.  """  
      self.DurationType:str = obj["DurationType"]
      """  This is will either be Hours or Days  """  
      self.RollChildMan:bool = obj["RollChildMan"]
      """  'Roll Child Manual Cost to Complete to this Level  """  
      self.RollChildBud:bool = obj["RollChildBud"]
      """  Roll Child Budgets to this Level  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Sort Sequence of the project phase.  This field controls where on the project tree the phase needs to be displayed.  """  
      self.MeasuredWorkID:str = obj["MeasuredWorkID"]
      """  Reference to the Measured Work header.  It is used to collect the cost to determine if the Measured Work was profitable or not.  """  
      self.TotQuotODCCost:int = obj["TotQuotODCCost"]
      """  Total quoted other direct cost for the Project phase.  """  
      self.ManEstCTCODCCost:int = obj["ManEstCTCODCCost"]
      """  Other direct cost manual CTC  """  
      self.TotCTCODCCost:int = obj["TotCTCODCCost"]
      """  Total calculated cost to complete other direct cost for the Project phase.  """  
      self.BudTotODCCost:int = obj["BudTotODCCost"]
      """  Other direct cost Budget Total  """  
      self.TimeApprovalsMethod:str = obj["TimeApprovalsMethod"]
      """  Defines the Approvals Method for Time related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for Time transactions related to this WBS Phase.  """  
      self.ExpenseApprovalsMethod:str = obj["ExpenseApprovalsMethod"]
      """  Defines the Approvals Method for Expenses related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for Expense transactions related to this WBS Phase.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RevMethod:str = obj["RevMethod"]
      """  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery.  """  
      self.WorkResDesc:str = obj["WorkResDesc"]
      self.StatusDesc:str = obj["StatusDesc"]
      self.GTActualCost:int = obj["GTActualCost"]
      self.GTBudgetCost:int = obj["GTBudgetCost"]
      self.GTCalculatedCost:int = obj["GTCalculatedCost"]
      self.GTEstimatedCost:int = obj["GTEstimatedCost"]
      self.GTManualCost:int = obj["GTManualCost"]
      self.GTQuotedCost:int = obj["GTQuotedCost"]
      self.createWBSJob:bool = obj["createWBSJob"]
      self.PhaseDesc:str = obj["PhaseDesc"]
      self.TimeWFGroupIDDescription:str = obj["TimeWFGroupIDDescription"]
      self.ExpenseWFGroupIDDescription:str = obj["ExpenseWFGroupIDDescription"]
      self.EnableApprovals:bool = obj["EnableApprovals"]
      self.TimeDefTaskSetID:str = obj["TimeDefTaskSetID"]
      self.ExpenseDefTaskSetID:str = obj["ExpenseDefTaskSetID"]
      self.ExpenseTaskSetDescription:str = obj["ExpenseTaskSetDescription"]
      self.TimeTaskSetDescription:str = obj["TimeTaskSetDescription"]
      self.EnableUpdOper:bool = obj["EnableUpdOper"]
      """  Flag to indicate whether the PPhaseOper for this ProjPhase should allow updates based on the status of the WBSJobNum.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      """  External field to create a WBS Phase Combo.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjPhaseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.StartDate:str = obj["StartDate"]
      """  Task start date.  """  
      self.DueDate:str = obj["DueDate"]
      """  Task due date.  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Must be greater than or equal to 0.  """  
      self.DateComplete:str = obj["DateComplete"]
      """  Date this task was complete.  """  
      self.PhaseStatus:str = obj["PhaseStatus"]
      """  Valid values are "N" = Not started, "I" = In Process, "C" = Completed.  """  
      self.Duration:int = obj["Duration"]
      """  This is the duration of the WBS Phase. On the UK software this currently uses field Number09  """  
      self.WBSJobNum:str = obj["WBSJobNum"]
      """  Reference to the job number created for the WBS Phase.  """  
      self.ParentPhase:str = obj["ParentPhase"]
      """  This is the parent phase for this WBS Phase. On the UK software this currently uses field ShortChar01  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back a alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.BudTotLbrHours:int = obj["BudTotLbrHours"]
      """  Total budget labour hours for the Project phase  """  
      self.BudTotBurHrs:int = obj["BudTotBurHrs"]
      """  Total budget burden hours for the Project phase.  """  
      self.BudTotLbrCost:int = obj["BudTotLbrCost"]
      """  Total budget labour cost for the Project phase. This is production and setup combined.  """  
      self.BudTotBurCost:int = obj["BudTotBurCost"]
      """  Total budget burden cost for the Project phase. This is production and setup combined.  """  
      self.BudTotSubCost:int = obj["BudTotSubCost"]
      """  Total budget subcontract costs for the Project phase  """  
      self.BudTotMtlCost:int = obj["BudTotMtlCost"]
      """  Total budget material costs for the Project phase  """  
      self.BudTotMtlBurCost:int = obj["BudTotMtlBurCost"]
      """  Total budget material burden costs for the Project phase.  """  
      self.TotEstLbrHrs:int = obj["TotEstLbrHrs"]
      """  Total estimated labour hours for the Project phase  """  
      self.TotEstBurdenHrs:int = obj["TotEstBurdenHrs"]
      """  Total estimated burden hours for the Project phase  """  
      self.TotEstLbrCost:int = obj["TotEstLbrCost"]
      """  Total estimated labour cost for the Project phase. This is production and setup combined.  """  
      self.TotEstSubContCost:int = obj["TotEstSubContCost"]
      """  Total estimated subcontract costs for the Project phase  """  
      self.TotEstMtlCost:int = obj["TotEstMtlCost"]
      """  Total estimated material costs for the Project phase  """  
      self.TotActLbrHrs:int = obj["TotActLbrHrs"]
      """  Total actual labour hours for the Project phase  """  
      self.TotActBurHrs:int = obj["TotActBurHrs"]
      """  Total actual burden hours for the Project phase  """  
      self.TotActLbrCost:int = obj["TotActLbrCost"]
      """  Total actual labour cost for the Project phase. This is production and setup combined.  """  
      self.TotActBurCost:int = obj["TotActBurCost"]
      """  Total actual burden cost for the Project phase. This is production and setup combined.  """  
      self.TotActSubContCost:int = obj["TotActSubContCost"]
      """  Total actual subcontract costs for the Project phase.  """  
      self.TotActMtlCost:int = obj["TotActMtlCost"]
      """  Total actual material costs for the Project phase  """  
      self.TotActMtlBurCost:int = obj["TotActMtlBurCost"]
      """  Total actual material burden costs for the Project phase.  """  
      self.ManEstCtcLbrHrs:int = obj["ManEstCtcLbrHrs"]
      """  Manually entered estimate to complete for the labour hours for the project phase  """  
      self.ManEstCtcBurHrs:int = obj["ManEstCtcBurHrs"]
      """  Manually entered estimate to complete for the burden hours.  """  
      self.ManEstCtcLbrCost:int = obj["ManEstCtcLbrCost"]
      """  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project phase.  """  
      self.ManEstCtcBurCost:int = obj["ManEstCtcBurCost"]
      """  Manually entered estimate to complete for the burden cost for the project phase.  """  
      self.ManEstCtcSubConCost:int = obj["ManEstCtcSubConCost"]
      """  Manually entered estimate to complete for the Subcontract cost for the project phase.  """  
      self.ManEstCtcMtlCost:int = obj["ManEstCtcMtlCost"]
      """  Manually entered estimate to complete for the material cost for the project phase.  """  
      self.ManEstCtcMtlBurCost:int = obj["ManEstCtcMtlBurCost"]
      """  Manually entered estimate to complete for the material burden cost for the project phase.  """  
      self.TotCtcLbrHours:int = obj["TotCtcLbrHours"]
      """  Total calculated cost to complete labour hours for the Project phase.  """  
      self.TotCtcBurHours:int = obj["TotCtcBurHours"]
      """  Total calculated cost to complete burden hours for the Project phase.  """  
      self.TotCtcLbrCost:int = obj["TotCtcLbrCost"]
      """  Total calculated cost to complete labour cost for the Project phase. This will be both production and setup.  """  
      self.TotCtcBurCost:int = obj["TotCtcBurCost"]
      """  Total calculated cost to complete burden cost for the Project phase. This will be both production and setup.  """  
      self.TotCtcSubConCost:int = obj["TotCtcSubConCost"]
      """  Total calculated cost to complete subcontract cost for the Project phase.  """  
      self.TotCtcMtlCost:int = obj["TotCtcMtlCost"]
      """  Total calculated cost to complete material cost for the Project phase.  """  
      self.TotCtcMtlBurCost:int = obj["TotCtcMtlBurCost"]
      """  Total calculated cost to complete material burden cost for the Project phase.  """  
      self.TotQuotLbrHrs:int = obj["TotQuotLbrHrs"]
      """  Total quoted labour hours for the Project phase  """  
      self.TotQuotBurHrs:int = obj["TotQuotBurHrs"]
      """  Total quoted burden hours for the Project phase.  """  
      self.TotQuotLbrCost:int = obj["TotQuotLbrCost"]
      """  Total quoted labour cost for the Project phase. This will be both production and setup.  """  
      self.TotQuotBurCost:int = obj["TotQuotBurCost"]
      """  Total quoted burden cost for the Project phase. This will be both production and setup.  """  
      self.TotQuotSubContCost:int = obj["TotQuotSubContCost"]
      """  Total quoted subcontract cost for the Project phase.  """  
      self.TotQuotMtlCost:int = obj["TotQuotMtlCost"]
      """  Total quoted material cost for the Project phase.  """  
      self.TotQuotMtlBurCost:int = obj["TotQuotMtlBurCost"]
      """  Total quoted material burden cost for the Project phase.  """  
      self.Level:int = obj["Level"]
      """  This holds the bom level of the phase reletive to the parent.  """  
      self.DurationType:str = obj["DurationType"]
      """  This is will either be Hours or Days  """  
      self.TotEstBurCost:int = obj["TotEstBurCost"]
      """  Total estimated burden cost for the Project phase. This is production and setup combined.  """  
      self.TotEstMtlBurCost:int = obj["TotEstMtlBurCost"]
      """  Total estimated material burden costs for the Project phase  """  
      self.RollChildMan:bool = obj["RollChildMan"]
      """  'Roll Child Manual Cost to Complete to this Level  """  
      self.RollChildBud:bool = obj["RollChildBud"]
      """  Roll Child Budgets to this Level  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Sort Sequence of the project phase.  This field controls where on the project tree the phase needs to be displayed.  """  
      self.MeasuredWorkID:str = obj["MeasuredWorkID"]
      """  Reference to the Measured Work header.  It is used to collect the cost to determine if the Measured Work was profitable or not.  """  
      self.TotQuotODCCost:int = obj["TotQuotODCCost"]
      """  Total quoted other direct cost for the Project phase.  """  
      self.TotEstODCCost:int = obj["TotEstODCCost"]
      """  Total estimated other direct costs for the Project phase  """  
      self.TotActODCCost:int = obj["TotActODCCost"]
      """  Total actual other direct costs for the Project phase.  """  
      self.ManEstCTCODCCost:int = obj["ManEstCTCODCCost"]
      """  Other direct cost manual CTC  """  
      self.TotCTCODCCost:int = obj["TotCTCODCCost"]
      """  Total calculated cost to complete other direct cost for the Project phase.  """  
      self.BudTotODCCost:int = obj["BudTotODCCost"]
      """  Other direct cost Budget Total  """  
      self.TimeApprovalsMethod:str = obj["TimeApprovalsMethod"]
      """  Defines the Approvals Method for Time related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for Time transactions related to this WBS Phase.  """  
      self.ExpenseApprovalsMethod:str = obj["ExpenseApprovalsMethod"]
      """  Defines the Approvals Method for Expenses related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for Expense transactions related to this WBS Phase.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvMethod:str = obj["InvMethod"]
      """  Invoicing Method  """  
      self.RevMethod:str = obj["RevMethod"]
      """  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales Order Line  """  
      self.WasRecInvoiced:bool = obj["WasRecInvoiced"]
      """  If any activity of the job assigned to the Phase has been recognized or invoiced  """  
      self.LastBuildWBSPhaseAnalysisDate:str = obj["LastBuildWBSPhaseAnalysisDate"]
      """  Date of last Build WBS Phase Analysis run.  """  
      self.PercentageOfCompletion:int = obj["PercentageOfCompletion"]
      """  Percentage of Completion  """  
      self.ToBeRecognizedLbrCost:int = obj["ToBeRecognizedLbrCost"]
      """  Labor Cost To Be Recognized  """  
      self.ToBeRecognizedBurCost:int = obj["ToBeRecognizedBurCost"]
      """  Burden Cost To Be Recognized  """  
      self.ToBeRecognizedMtlCost:int = obj["ToBeRecognizedMtlCost"]
      """  Material Cost To Be Recognized  """  
      self.ToBeRecognizedSubCost:int = obj["ToBeRecognizedSubCost"]
      """  Subcontract Cost To Be Recognized  """  
      self.ToBeRecognizedMtlBurCost:int = obj["ToBeRecognizedMtlBurCost"]
      """  Material Burden Cost To Be Recognized  """  
      self.ToBeRecognizedODCCost:int = obj["ToBeRecognizedODCCost"]
      """  ODC Cost To Be Recognized  """  
      self.ToBeRecognizedRevenue:int = obj["ToBeRecognizedRevenue"]
      """  Revenue To Be Recognized  """  
      self.RecognizeRevenueAtChildPhaseLevel:bool = obj["RecognizeRevenueAtChildPhaseLevel"]
      """  When true,  Recognize Revenue separately at Child WBS Phases.  When false, Recognize Revenue for this phase and all child phases at this level.  """  
      self.RollBudgetsToWBSPhase:bool = obj["RollBudgetsToWBSPhase"]
      """  To control if the project phase budget values are to be rolled up to the project phase.  """  
      self.TotWBSPhaseRev:int = obj["TotWBSPhaseRev"]
      """  TotWBSPhaseRev  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  The sales category code used in the Revenue recognition process.  """  
      self.ActMtlNonJobCost:int = obj["ActMtlNonJobCost"]
      """  ActMtlNonJobCost  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  AsOfDate  """  
      self.BdnRecSeqPosted:int = obj["BdnRecSeqPosted"]
      """  Number of Recalculation of burden amounts posted to GL by Revenue Recognition process  """  
      self.BdnRecSeqLastAdded:int = obj["BdnRecSeqLastAdded"]
      """  Number of Recalculation of burden amounts created by Revenue Recognition process  """  
      self.BdnRevenueAutoToday:int = obj["BdnRevenueAutoToday"]
      """  Sum of all Actual Burden Charges posted by today  """  
      self.BillingToDate:int = obj["BillingToDate"]
      """  BillingToDate  """  
      self.BuildAnalysis:bool = obj["BuildAnalysis"]
      """  BuildAnalysis  """  
      self.BurdenCostOfSales:int = obj["BurdenCostOfSales"]
      """  The burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActBurdenCost  """  
      self.BurdenLbrCstToDate:int = obj["BurdenLbrCstToDate"]
      """  BurdenLbrCstToDate  """  
      self.BurdenRecAutoCstTodate:int = obj["BurdenRecAutoCstTodate"]
      """  The burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.BurdenRecManCstTodate:int = obj["BurdenRecManCstTodate"]
      """  The burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process  """  
      self.BurManPosted:int = obj["BurManPosted"]
      """  BurManPosted  """  
      self.BurPur:int = obj["BurPur"]
      """  BurPur  """  
      self.EstBurdenCost:int = obj["EstBurdenCost"]
      """  Estimated burden cost.  """  
      self.EstBurdenHours:int = obj["EstBurdenHours"]
      """  Estimated burden hours.  """  
      self.EstLaborCost:int = obj["EstLaborCost"]
      """  Estimated labor cost.  """  
      self.EstLaborHours:int = obj["EstLaborHours"]
      """  Estimated labor hours.  """  
      self.EstMtlBurdenCost:int = obj["EstMtlBurdenCost"]
      """  Estimated material burden cost.  """  
      self.EstMtlCost:int = obj["EstMtlCost"]
      """  Estimated material cost.  """  
      self.EstODCCost:int = obj["EstODCCost"]
      """  Estimated other direct cost.  """  
      self.EstSubcontractCost:int = obj["EstSubcontractCost"]
      """  Estimated subcontract cost.  """  
      self.LaborCostOfSales:int = obj["LaborCostOfSales"]
      """  The labour costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActLaborCost.  """  
      self.LaborLbrCstToDate:int = obj["LaborLbrCstToDate"]
      """  LaborLbrCstToDate  """  
      self.LaborRecAutoCstTodate:int = obj["LaborRecAutoCstTodate"]
      """  The labour costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.LaborRecManCstTodate:int = obj["LaborRecManCstTodate"]
      """  The labor costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.LbrManPosted:int = obj["LbrManPosted"]
      """  LbrManPosted  """  
      self.LbrPur:int = obj["LbrPur"]
      """  LbrPur  """  
      self.MaterialCostOfSales:int = obj["MaterialCostOfSales"]
      """  The material costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of Material with a linesource of COS with value from ProjectAnalysis.ActMatCost.  """  
      self.MaterialRecAutoCstTodate:int = obj["MaterialRecAutoCstTodate"]
      """  The material costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.MaterialRecManCstTodate:int = obj["MaterialRecManCstTodate"]
      """  The material costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.MtlBurdenCostOfSales:int = obj["MtlBurdenCostOfSales"]
      """  The material burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActMatBurdenCost  """  
      self.MtlBurdenRecAutoCstTodate:int = obj["MtlBurdenRecAutoCstTodate"]
      """  The material burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  """  
      self.MtlBurdenRecManCstTodate:int = obj["MtlBurdenRecManCstTodate"]
      """  The material burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.MtlBurManPosted:int = obj["MtlBurManPosted"]
      """  MtlBurManPosted  """  
      self.MtlBurPur:int = obj["MtlBurPur"]
      """  MtlBurPur  """  
      self.MtlManPosted:int = obj["MtlManPosted"]
      """  MtlManPosted  """  
      self.MtlPur:int = obj["MtlPur"]
      """  MtlPur  """  
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      """  NextTmpInvcNum  """  
      self.ODCManPosted:int = obj["ODCManPosted"]
      """  ODCManPosted  """  
      self.ODCPur:int = obj["ODCPur"]
      """  ODCPur  """  
      self.ODCRecAutoCstToDate:int = obj["ODCRecAutoCstToDate"]
      """  Other Direct cost Recognition to Date  """  
      self.ODCRecManCstTodate:int = obj["ODCRecManCstTodate"]
      """  Other Direct Cost Manual Recognition to Date  """  
      self.RecManPosted:int = obj["RecManPosted"]
      """  RecManPosted  """  
      self.RecogToDtBilling:int = obj["RecogToDtBilling"]
      """  RecogToDtBilling  """  
      self.RecogToDtLbk:int = obj["RecogToDtLbk"]
      """  RecogToDtLbk  """  
      self.RecogToDtManual:int = obj["RecogToDtManual"]
      """  RecogToDtManual  """  
      self.RetentionDt:int = obj["RetentionDt"]
      """  RetentionDt  """  
      self.RevenueRecAutoToDate:int = obj["RevenueRecAutoToDate"]
      """  The revenue that has been recognised to date for the project. This is revenue that has been invoiced against the sales order either as an advanced billing or a shipment. This is the sum of ProjectAnalysis records with a Linecode of Revenue with a linesource of Invoice with value from ProjectAnalysis.ActMatCost.  """  
      self.RevenueRecManToDate:int = obj["RevenueRecManToDate"]
      """  The revenue that has been recognised to date for the project. This is revenue that has been manually recognised using this process.  """  
      self.Reverse:str = obj["Reverse"]
      """  Reverse  """  
      self.RollManEstToCpte:bool = obj["RollManEstToCpte"]
      """  RollManEstToCpte  """  
      self.SubCManPosted:int = obj["SubCManPosted"]
      """  SubCManPosted  """  
      self.SubConCostOfSales:int = obj["SubConCostOfSales"]
      """  SubConCostOfSales  """  
      self.SubConRecAutoCstTodate:int = obj["SubConRecAutoCstTodate"]
      """  SubConRecAutoCstTodate  """  
      self.SubConRecManCstTodate:int = obj["SubConRecManCstTodate"]
      """  SubConRecManCstTodate  """  
      self.SubPur:int = obj["SubPur"]
      """  SubPur  """  
      self.ConTotValue:int = obj["ConTotValue"]
      """  Total contract value for the WBS Phase.  """  
      self.DocConTotValue:int = obj["DocConTotValue"]
      """  Total contract value for the WBS Phase in the Document currency.  """  
      self.Rpt1ConTotValue:int = obj["Rpt1ConTotValue"]
      """  Total contract value for the WBS Phase in the Reporting currency.  """  
      self.Rpt2ConTotValue:int = obj["Rpt2ConTotValue"]
      """  Total contract value for the WBS Phase in the Reporting currency.  """  
      self.Rpt3ConTotValue:int = obj["Rpt3ConTotValue"]
      """  Total contract value for the WBS Phase in the Reporting currency.  """  
      self.ConTotValueNet:int = obj["ConTotValueNet"]
      """  Net total contract value for the WBS Phase.  """  
      self.DocConTotValueNet:int = obj["DocConTotValueNet"]
      """  Net total contract value for the WBS Phase in the Document currency.  """  
      self.Rpt1ConTotValueNet:int = obj["Rpt1ConTotValueNet"]
      """  Net total contract value for the WBS Phase in the Reporting currency.  """  
      self.Rpt2ConTotValueNet:int = obj["Rpt2ConTotValueNet"]
      """  Net total contract value for the WBS Phase in the Reporting currency.  """  
      self.Rpt3ConTotValueNet:int = obj["Rpt3ConTotValueNet"]
      """  Net total contract value for the WBS Phase in the Reporting currency.  """  
      self.CloseWBSJob:bool = obj["CloseWBSJob"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocBudTotBurCost:int = obj["DocBudTotBurCost"]
      self.DocBudTotLbrCost:int = obj["DocBudTotLbrCost"]
      self.DocBudTotMtlBurCost:int = obj["DocBudTotMtlBurCost"]
      self.DocBudTotMtlCost:int = obj["DocBudTotMtlCost"]
      self.DocBudTotODCCost:int = obj["DocBudTotODCCost"]
      self.DocGTActualCost:int = obj["DocGTActualCost"]
      self.DocGTBudgetCost:int = obj["DocGTBudgetCost"]
      self.DocGTCalculatedCost:int = obj["DocGTCalculatedCost"]
      self.DocGTEstimatedCost:int = obj["DocGTEstimatedCost"]
      self.DocGTManualCost:int = obj["DocGTManualCost"]
      self.DocGTQuotedCost:int = obj["DocGTQuotedCost"]
      self.DocManEstCtcBurCost:int = obj["DocManEstCtcBurCost"]
      self.DocManEstCtcLbrCost:int = obj["DocManEstCtcLbrCost"]
      self.DocManEstCtcMtlBurCost:int = obj["DocManEstCtcMtlBurCost"]
      self.DocManEstCtcMtlCost:int = obj["DocManEstCtcMtlCost"]
      self.DocManEstCTCODCCost:int = obj["DocManEstCTCODCCost"]
      self.DocManEstCtcSubConCost:int = obj["DocManEstCtcSubConCost"]
      self.DocProjectedTotalBurCost:int = obj["DocProjectedTotalBurCost"]
      self.DocProjectedTotalCost:int = obj["DocProjectedTotalCost"]
      self.DocProjectedTotalLbrCost:int = obj["DocProjectedTotalLbrCost"]
      self.DocProjectedTotalMtlBurCost:int = obj["DocProjectedTotalMtlBurCost"]
      self.DocProjectedTotalMtlCost:int = obj["DocProjectedTotalMtlCost"]
      self.DocProjectedTotalODCCost:int = obj["DocProjectedTotalODCCost"]
      self.DocProjectedTotalSubContCost:int = obj["DocProjectedTotalSubContCost"]
      self.DocTotActSubContCost:int = obj["DocTotActSubContCost"]
      self.DocTotCtcBurCost:int = obj["DocTotCtcBurCost"]
      self.DocTotCtcLbrCost:int = obj["DocTotCtcLbrCost"]
      self.DocTotCtcMtlBurCost:int = obj["DocTotCtcMtlBurCost"]
      self.DocTotCtcMtlCost:int = obj["DocTotCtcMtlCost"]
      self.DocTotCTCODCCost:int = obj["DocTotCTCODCCost"]
      self.DocTotCtcSubConCost:int = obj["DocTotCtcSubConCost"]
      self.DocTotEstBurCost:int = obj["DocTotEstBurCost"]
      self.DocTotEstLbrCost:int = obj["DocTotEstLbrCost"]
      self.DocTotEstMtlBurCost:int = obj["DocTotEstMtlBurCost"]
      self.DocTotEstMtlCost:int = obj["DocTotEstMtlCost"]
      self.DocTotEstODCCost:int = obj["DocTotEstODCCost"]
      self.DocTotEstSubContCost:int = obj["DocTotEstSubContCost"]
      self.DocTotQuotBurCost:int = obj["DocTotQuotBurCost"]
      self.DocTotQuotLbrCost:int = obj["DocTotQuotLbrCost"]
      self.DocTotQuotMtlBurCost:int = obj["DocTotQuotMtlBurCost"]
      self.DocTotQuotMtlCost:int = obj["DocTotQuotMtlCost"]
      self.DocTotQuotODCCost:int = obj["DocTotQuotODCCost"]
      self.DocTotQuotSubContCost:int = obj["DocTotQuotSubContCost"]
      self.EnableApprovals:bool = obj["EnableApprovals"]
      self.EnableRecognizeRevenueAtChildPhaseLevel:bool = obj["EnableRecognizeRevenueAtChildPhaseLevel"]
      """  This flag indicates whether ProjPhase.RecognizeRevenueAtChildPhaseLevel should be enabled in the UI.  """  
      self.EnableUpdOper:bool = obj["EnableUpdOper"]
      """  Flag to indicate whether the PPhaseOper for this ProjPhase should allow updates based on the status of the WBSJobNum.  """  
      self.EngineerWBSJob:bool = obj["EngineerWBSJob"]
      self.ExpenseDefTaskSetID:str = obj["ExpenseDefTaskSetID"]
      self.ExpenseTaskSetDescription:str = obj["ExpenseTaskSetDescription"]
      self.ExpenseWFGroupIDDescription:str = obj["ExpenseWFGroupIDDescription"]
      self.GTActualCost:int = obj["GTActualCost"]
      self.GTBudgetCost:int = obj["GTBudgetCost"]
      self.GTCalculatedCost:int = obj["GTCalculatedCost"]
      self.GTEstimatedCost:int = obj["GTEstimatedCost"]
      self.GTManualCost:int = obj["GTManualCost"]
      self.GTQuotedCost:int = obj["GTQuotedCost"]
      self.IsRootPhase:bool = obj["IsRootPhase"]
      self.JobDueDate:str = obj["JobDueDate"]
      """  used to display Due date of the WBS phase job when scheduled  """  
      self.JobStartDate:str = obj["JobStartDate"]
      """  used to display Start date of the WBS phase job when scheduled  """  
      self.ParentPhaseIsRootPhase:bool = obj["ParentPhaseIsRootPhase"]
      self.PhaseDesc:str = obj["PhaseDesc"]
      self.PInvMethod:str = obj["PInvMethod"]
      self.PRevMethod:str = obj["PRevMethod"]
      self.ProjectedTotalBurCost:int = obj["ProjectedTotalBurCost"]
      self.ProjectedTotalCost:int = obj["ProjectedTotalCost"]
      self.ProjectedTotalLbrCost:int = obj["ProjectedTotalLbrCost"]
      self.ProjectedTotalMtlBurCost:int = obj["ProjectedTotalMtlBurCost"]
      self.ProjectedTotalMtlCost:int = obj["ProjectedTotalMtlCost"]
      self.ProjectedTotalODCCost:int = obj["ProjectedTotalODCCost"]
      self.ProjectedTotalSubContCost:int = obj["ProjectedTotalSubContCost"]
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      """  External Field To create a WBS Phase Combo  """  
      self.ReleaseWBSJob:bool = obj["ReleaseWBSJob"]
      self.Rpt1BudTotBurCost:int = obj["Rpt1BudTotBurCost"]
      self.Rpt1BudTotLbrCost:int = obj["Rpt1BudTotLbrCost"]
      self.Rpt1BudTotMtlBurCost:int = obj["Rpt1BudTotMtlBurCost"]
      self.Rpt1BudTotMtlCost:int = obj["Rpt1BudTotMtlCost"]
      self.Rpt1BudTotODCCost:int = obj["Rpt1BudTotODCCost"]
      self.Rpt1BudTotSubCost:int = obj["Rpt1BudTotSubCost"]
      self.Rpt1GTActualCost:int = obj["Rpt1GTActualCost"]
      self.Rpt1GTBudgetCost:int = obj["Rpt1GTBudgetCost"]
      self.Rpt1GTCalculatedCost:int = obj["Rpt1GTCalculatedCost"]
      self.Rpt1GTEstimatedCost:int = obj["Rpt1GTEstimatedCost"]
      self.Rpt1GTManualCost:int = obj["Rpt1GTManualCost"]
      self.Rpt1GTQuotedCost:int = obj["Rpt1GTQuotedCost"]
      self.Rpt1ManEstCtcBurCost:int = obj["Rpt1ManEstCtcBurCost"]
      self.Rpt1ManEstCtcLbrCost:int = obj["Rpt1ManEstCtcLbrCost"]
      self.Rpt1ManEstCtcMtlBurCost:int = obj["Rpt1ManEstCtcMtlBurCost"]
      self.Rpt1ManEstCtcMtlCost:int = obj["Rpt1ManEstCtcMtlCost"]
      self.Rpt1ManEstCTCODCCost:int = obj["Rpt1ManEstCTCODCCost"]
      self.Rpt1ManEstCtcSubConCost:int = obj["Rpt1ManEstCtcSubConCost"]
      self.Rpt1ProjectedTotalBurCost:int = obj["Rpt1ProjectedTotalBurCost"]
      self.Rpt1ProjectedTotalCost:int = obj["Rpt1ProjectedTotalCost"]
      self.Rpt1ProjectedTotalLbrCost:int = obj["Rpt1ProjectedTotalLbrCost"]
      self.Rpt1ProjectedTotalMtlBurCost:int = obj["Rpt1ProjectedTotalMtlBurCost"]
      self.Rpt1ProjectedTotalMtlCost:int = obj["Rpt1ProjectedTotalMtlCost"]
      self.Rpt1ProjectedTotalODCCost:int = obj["Rpt1ProjectedTotalODCCost"]
      self.Rpt1ProjectedTotalSubContCost:int = obj["Rpt1ProjectedTotalSubContCost"]
      self.Rpt1TotActBurCost:int = obj["Rpt1TotActBurCost"]
      self.Rpt1TotActLbrCost:int = obj["Rpt1TotActLbrCost"]
      self.Rpt1TotActMtlBurCost:int = obj["Rpt1TotActMtlBurCost"]
      self.Rpt1TotActMtlCost:int = obj["Rpt1TotActMtlCost"]
      self.Rpt1TotActODCCost:int = obj["Rpt1TotActODCCost"]
      self.Rpt1TotActSubContCost:int = obj["Rpt1TotActSubContCost"]
      self.Rpt1TotCtcBurCost:int = obj["Rpt1TotCtcBurCost"]
      self.Rpt1TotCtcLbrCost:int = obj["Rpt1TotCtcLbrCost"]
      self.Rpt1TotCtcMtlBurCost:int = obj["Rpt1TotCtcMtlBurCost"]
      self.Rpt1TotCtcMtlCost:int = obj["Rpt1TotCtcMtlCost"]
      self.Rpt1TotCTCODCCost:int = obj["Rpt1TotCTCODCCost"]
      self.Rpt1TotCtcSubConCost:int = obj["Rpt1TotCtcSubConCost"]
      self.Rpt1TotEstBurCost:int = obj["Rpt1TotEstBurCost"]
      self.Rpt1TotEstLbrCost:int = obj["Rpt1TotEstLbrCost"]
      self.Rpt1TotEstMtlBurCost:int = obj["Rpt1TotEstMtlBurCost"]
      self.Rpt1TotEstMtlCost:int = obj["Rpt1TotEstMtlCost"]
      self.Rpt1TotEstODCCost:int = obj["Rpt1TotEstODCCost"]
      self.Rpt1TotEstSubContCost:int = obj["Rpt1TotEstSubContCost"]
      self.Rpt1TotQuotBurCost:int = obj["Rpt1TotQuotBurCost"]
      self.Rpt1TotQuotLbrCost:int = obj["Rpt1TotQuotLbrCost"]
      self.Rpt1TotQuotMtlBurCost:int = obj["Rpt1TotQuotMtlBurCost"]
      self.Rpt1TotQuotMtlCost:int = obj["Rpt1TotQuotMtlCost"]
      self.Rpt1TotQuotODCCost:int = obj["Rpt1TotQuotODCCost"]
      self.Rpt1TotQuotSubContCost:int = obj["Rpt1TotQuotSubContCost"]
      self.Rpt2BudTotBurCost:int = obj["Rpt2BudTotBurCost"]
      self.Rpt2BudTotLbrCost:int = obj["Rpt2BudTotLbrCost"]
      self.Rpt2BudTotMtlBurCost:int = obj["Rpt2BudTotMtlBurCost"]
      self.Rpt2BudTotMtlCost:int = obj["Rpt2BudTotMtlCost"]
      self.Rpt2BudTotODCCost:int = obj["Rpt2BudTotODCCost"]
      self.Rpt2BudTotSubCost:int = obj["Rpt2BudTotSubCost"]
      self.Rpt2GTActualCost:int = obj["Rpt2GTActualCost"]
      self.Rpt2GTBudgetCost:int = obj["Rpt2GTBudgetCost"]
      self.Rpt2GTCalculatedCost:int = obj["Rpt2GTCalculatedCost"]
      self.Rpt2GTEstimatedCost:int = obj["Rpt2GTEstimatedCost"]
      self.Rpt2GTManualCost:int = obj["Rpt2GTManualCost"]
      self.Rpt2GTQuotedCost:int = obj["Rpt2GTQuotedCost"]
      self.Rpt2ManEstCtcBurCost:int = obj["Rpt2ManEstCtcBurCost"]
      self.Rpt2ManEstCtcLbrCost:int = obj["Rpt2ManEstCtcLbrCost"]
      self.Rpt2ManEstCtcMtlBurCost:int = obj["Rpt2ManEstCtcMtlBurCost"]
      self.Rpt2ManEstCtcMtlCost:int = obj["Rpt2ManEstCtcMtlCost"]
      self.Rpt2ManEstCTCODCCost:int = obj["Rpt2ManEstCTCODCCost"]
      self.Rpt2ManEstCtcSubConCost:int = obj["Rpt2ManEstCtcSubConCost"]
      self.Rpt2ProjectedTotalBurCost:int = obj["Rpt2ProjectedTotalBurCost"]
      self.Rpt2ProjectedTotalCost:int = obj["Rpt2ProjectedTotalCost"]
      self.Rpt2ProjectedTotalLbrCost:int = obj["Rpt2ProjectedTotalLbrCost"]
      self.Rpt2ProjectedTotalMtlBurCost:int = obj["Rpt2ProjectedTotalMtlBurCost"]
      self.Rpt2ProjectedTotalMtlCost:int = obj["Rpt2ProjectedTotalMtlCost"]
      self.Rpt2ProjectedTotalODCCost:int = obj["Rpt2ProjectedTotalODCCost"]
      self.Rpt2ProjectedTotalSubContCost:int = obj["Rpt2ProjectedTotalSubContCost"]
      self.Rpt2TotActBurCost:int = obj["Rpt2TotActBurCost"]
      self.Rpt2TotActLbrCost:int = obj["Rpt2TotActLbrCost"]
      self.Rpt2TotActMtlBurCost:int = obj["Rpt2TotActMtlBurCost"]
      self.Rpt2TotActMtlCost:int = obj["Rpt2TotActMtlCost"]
      self.Rpt2TotActODCCost:int = obj["Rpt2TotActODCCost"]
      self.Rpt2TotActSubContCost:int = obj["Rpt2TotActSubContCost"]
      self.Rpt2TotCtcBurCost:int = obj["Rpt2TotCtcBurCost"]
      self.Rpt2TotCtcLbrCost:int = obj["Rpt2TotCtcLbrCost"]
      self.Rpt2TotCtcMtlBurCost:int = obj["Rpt2TotCtcMtlBurCost"]
      self.Rpt2TotCtcMtlCost:int = obj["Rpt2TotCtcMtlCost"]
      self.Rpt2TotCTCODCCost:int = obj["Rpt2TotCTCODCCost"]
      self.Rpt2TotCtcSubConCost:int = obj["Rpt2TotCtcSubConCost"]
      self.Rpt2TotEstBurCost:int = obj["Rpt2TotEstBurCost"]
      self.Rpt2TotEstLbrCost:int = obj["Rpt2TotEstLbrCost"]
      self.Rpt2TotEstMtlBurCost:int = obj["Rpt2TotEstMtlBurCost"]
      self.Rpt2TotEstMtlCost:int = obj["Rpt2TotEstMtlCost"]
      self.Rpt2TotEstODCCost:int = obj["Rpt2TotEstODCCost"]
      self.Rpt2TotEstSubContCost:int = obj["Rpt2TotEstSubContCost"]
      self.Rpt2TotQuotBurCost:int = obj["Rpt2TotQuotBurCost"]
      self.Rpt2TotQuotLbrCost:int = obj["Rpt2TotQuotLbrCost"]
      self.Rpt2TotQuotMtlBurCost:int = obj["Rpt2TotQuotMtlBurCost"]
      self.Rpt2TotQuotMtlCost:int = obj["Rpt2TotQuotMtlCost"]
      self.Rpt2TotQuotODCCost:int = obj["Rpt2TotQuotODCCost"]
      self.Rpt2TotQuotSubContCost:int = obj["Rpt2TotQuotSubContCost"]
      self.Rpt3BudTotBurCost:int = obj["Rpt3BudTotBurCost"]
      self.Rpt3BudTotLbrCost:int = obj["Rpt3BudTotLbrCost"]
      self.Rpt3BudTotMtlBurCost:int = obj["Rpt3BudTotMtlBurCost"]
      self.Rpt3BudTotMtlCost:int = obj["Rpt3BudTotMtlCost"]
      self.Rpt3BudTotODCCost:int = obj["Rpt3BudTotODCCost"]
      self.Rpt3BudTotSubCost:int = obj["Rpt3BudTotSubCost"]
      self.Rpt3GTActualCost:int = obj["Rpt3GTActualCost"]
      self.Rpt3GTBudgetCost:int = obj["Rpt3GTBudgetCost"]
      self.Rpt3GTCalculatedCost:int = obj["Rpt3GTCalculatedCost"]
      self.Rpt3GTEstimatedCost:int = obj["Rpt3GTEstimatedCost"]
      self.Rpt3GTManualCost:int = obj["Rpt3GTManualCost"]
      self.Rpt3GTQuotedCost:int = obj["Rpt3GTQuotedCost"]
      self.Rpt3ManEstCtcBurCost:int = obj["Rpt3ManEstCtcBurCost"]
      self.Rpt3ManEstCtcLbrCost:int = obj["Rpt3ManEstCtcLbrCost"]
      self.Rpt3ManEstCtcMtlBurCost:int = obj["Rpt3ManEstCtcMtlBurCost"]
      self.Rpt3ManEstCtcMtlCost:int = obj["Rpt3ManEstCtcMtlCost"]
      self.Rpt3ManEstCTCODCCost:int = obj["Rpt3ManEstCTCODCCost"]
      self.Rpt3ManEstCtcSubConCost:int = obj["Rpt3ManEstCtcSubConCost"]
      self.Rpt3ProjectedTotalBurCost:int = obj["Rpt3ProjectedTotalBurCost"]
      self.Rpt3ProjectedTotalCost:int = obj["Rpt3ProjectedTotalCost"]
      self.Rpt3ProjectedTotalLbrCost:int = obj["Rpt3ProjectedTotalLbrCost"]
      self.Rpt3ProjectedTotalMtlBurCost:int = obj["Rpt3ProjectedTotalMtlBurCost"]
      self.Rpt3ProjectedTotalMtlCost:int = obj["Rpt3ProjectedTotalMtlCost"]
      self.Rpt3ProjectedTotalODCCost:int = obj["Rpt3ProjectedTotalODCCost"]
      self.Rpt3ProjectedTotalSubContCost:int = obj["Rpt3ProjectedTotalSubContCost"]
      self.Rpt3TotActBurCost:int = obj["Rpt3TotActBurCost"]
      self.Rpt3TotActLbrCost:int = obj["Rpt3TotActLbrCost"]
      self.Rpt3TotActMtlBurCost:int = obj["Rpt3TotActMtlBurCost"]
      self.Rpt3TotActMtlCost:int = obj["Rpt3TotActMtlCost"]
      self.Rpt3TotActODCCost:int = obj["Rpt3TotActODCCost"]
      self.Rpt3TotActSubContCost:int = obj["Rpt3TotActSubContCost"]
      self.Rpt3TotCtcBurCost:int = obj["Rpt3TotCtcBurCost"]
      self.Rpt3TotCtcLbrCost:int = obj["Rpt3TotCtcLbrCost"]
      self.Rpt3TotCtcMtlBurCost:int = obj["Rpt3TotCtcMtlBurCost"]
      self.Rpt3TotCtcMtlCost:int = obj["Rpt3TotCtcMtlCost"]
      self.Rpt3TotCTCODCCost:int = obj["Rpt3TotCTCODCCost"]
      self.Rpt3TotCtcSubConCost:int = obj["Rpt3TotCtcSubConCost"]
      self.Rpt3TotEstBurCost:int = obj["Rpt3TotEstBurCost"]
      self.Rpt3TotEstLbrCost:int = obj["Rpt3TotEstLbrCost"]
      self.Rpt3TotEstMtlBurCost:int = obj["Rpt3TotEstMtlBurCost"]
      self.Rpt3TotEstMtlCost:int = obj["Rpt3TotEstMtlCost"]
      self.Rpt3TotEstODCCost:int = obj["Rpt3TotEstODCCost"]
      self.Rpt3TotEstSubContCost:int = obj["Rpt3TotEstSubContCost"]
      self.Rpt3TotQuotBurCost:int = obj["Rpt3TotQuotBurCost"]
      self.Rpt3TotQuotLbrCost:int = obj["Rpt3TotQuotLbrCost"]
      self.Rpt3TotQuotMtlBurCost:int = obj["Rpt3TotQuotMtlBurCost"]
      self.Rpt3TotQuotMtlCost:int = obj["Rpt3TotQuotMtlCost"]
      self.Rpt3TotQuotODCCost:int = obj["Rpt3TotQuotODCCost"]
      self.Rpt3TotQuotSubContCost:int = obj["Rpt3TotQuotSubContCost"]
      self.StatusDesc:str = obj["StatusDesc"]
      self.TimeDefTaskSetID:str = obj["TimeDefTaskSetID"]
      self.TimeTaskSetDescription:str = obj["TimeTaskSetDescription"]
      self.TimeWFGroupIDDescription:str = obj["TimeWFGroupIDDescription"]
      self.WorkResDesc:str = obj["WorkResDesc"]
      self.DocBudTotSubCost:int = obj["DocBudTotSubCost"]
      self.DocTotActBurCost:int = obj["DocTotActBurCost"]
      self.DocTotActLbrCost:int = obj["DocTotActLbrCost"]
      self.DocTotActMtlBurCost:int = obj["DocTotActMtlBurCost"]
      self.DocTotActMtlCost:int = obj["DocTotActMtlCost"]
      self.DocTotActODCCost:int = obj["DocTotActODCCost"]
      self.ExpenseApprovalTasksTree:str = obj["ExpenseApprovalTasksTree"]
      self.TimeApprovalTasksTree:str = obj["TimeApprovalTasksTree"]
      self.BitFlag:int = obj["BitFlag"]
      self.ParentPhaseDescription:str = obj["ParentPhaseDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.ProjectType_c:str = obj["ProjectType_c"]
      self.ShipToNum_c:str = obj["ShipToNum_c"]
      self.ShipToSameAsProj_c:bool = obj["ShipToSameAsProj_c"]
      self.Price_c:int = obj["Price_c"]
      self.Discount_c:int = obj["Discount_c"]
      self.ResaleRevenue_c:int = obj["ResaleRevenue_c"]
      self.FreightRevenueAmt_c:int = obj["FreightRevenueAmt_c"]
      self.SalesTaxRevenue_c:int = obj["SalesTaxRevenue_c"]
      self.Approved_c:bool = obj["Approved_c"]
      self.ApprovedBy_c:str = obj["ApprovedBy_c"]
      self.ApprovedDate_c:str = obj["ApprovedDate_c"]
      self.PartNum_c:str = obj["PartNum_c"]
      self.PartDescription_c:str = obj["PartDescription_c"]
      self.CreateRelatedPhases_c:bool = obj["CreateRelatedPhases_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   projectID
   phaseID
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      self.phaseID:str = obj["phaseID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ProjPhaseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.StartDate:str = obj["StartDate"]
      """  Task start date.  """  
      self.DueDate:str = obj["DueDate"]
      """  Task due date.  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Must be greater than or equal to 0.  """  
      self.DateComplete:str = obj["DateComplete"]
      """  Date this task was complete.  """  
      self.PhaseStatus:str = obj["PhaseStatus"]
      """  Valid values are "N" = Not started, "I" = In Process, "C" = Completed.  """  
      self.Duration:int = obj["Duration"]
      """  This is the duration of the WBS Phase. On the UK software this currently uses field Number09  """  
      self.WBSJobNum:str = obj["WBSJobNum"]
      """  Reference to the job number created for the WBS Phase.  """  
      self.ParentPhase:str = obj["ParentPhase"]
      """  This is the parent phase for this WBS Phase. On the UK software this currently uses field ShortChar01  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back a alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.BudTotBurHrs:int = obj["BudTotBurHrs"]
      """  Total budget burden hours for the Project phase.  """  
      self.BudTotLbrCost:int = obj["BudTotLbrCost"]
      """  Total budget labour cost for the Project phase. This is production and setup combined.  """  
      self.BudTotBurCost:int = obj["BudTotBurCost"]
      """  Total budget burden cost for the Project phase. This is production and setup combined.  """  
      self.BudTotMtlCost:int = obj["BudTotMtlCost"]
      """  Total budget material costs for the Project phase  """  
      self.BudTotMtlBurCost:int = obj["BudTotMtlBurCost"]
      """  Total budget material burden costs for the Project phase.  """  
      self.ManEstCtcLbrHrs:int = obj["ManEstCtcLbrHrs"]
      """  Manually entered estimate to complete for the labour hours for the project phase  """  
      self.ManEstCtcBurHrs:int = obj["ManEstCtcBurHrs"]
      """  Manually entered estimate to complete for the burden hours.  """  
      self.ManEstCtcLbrCost:int = obj["ManEstCtcLbrCost"]
      """  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project phase.  """  
      self.ManEstCtcBurCost:int = obj["ManEstCtcBurCost"]
      """  Manually entered estimate to complete for the burden cost for the project phase.  """  
      self.ManEstCtcSubConCost:int = obj["ManEstCtcSubConCost"]
      """  Manually entered estimate to complete for the Subcontract cost for the project phase.  """  
      self.ManEstCtcMtlCost:int = obj["ManEstCtcMtlCost"]
      """  Manually entered estimate to complete for the material cost for the project phase.  """  
      self.ManEstCtcMtlBurCost:int = obj["ManEstCtcMtlBurCost"]
      """  Manually entered estimate to complete for the material burden cost for the project phase.  """  
      self.TotCtcLbrCost:int = obj["TotCtcLbrCost"]
      """  Total calculated cost to complete labour cost for the Project phase. This will be both production and setup.  """  
      self.TotCtcBurCost:int = obj["TotCtcBurCost"]
      """  Total calculated cost to complete burden cost for the Project phase. This will be both production and setup.  """  
      self.TotCtcSubConCost:int = obj["TotCtcSubConCost"]
      """  Total calculated cost to complete subcontract cost for the Project phase.  """  
      self.TotCtcMtlCost:int = obj["TotCtcMtlCost"]
      """  Total calculated cost to complete material cost for the Project phase.  """  
      self.TotCtcMtlBurCost:int = obj["TotCtcMtlBurCost"]
      """  Total calculated cost to complete material burden cost for the Project phase.  """  
      self.TotQuotLbrHrs:int = obj["TotQuotLbrHrs"]
      """  Total quoted labour hours for the Project phase  """  
      self.TotQuotBurHrs:int = obj["TotQuotBurHrs"]
      """  Total quoted burden hours for the Project phase.  """  
      self.TotQuotLbrCost:int = obj["TotQuotLbrCost"]
      """  Total quoted labour cost for the Project phase. This will be both production and setup.  """  
      self.TotQuotBurCost:int = obj["TotQuotBurCost"]
      """  Total quoted burden cost for the Project phase. This will be both production and setup.  """  
      self.TotQuotSubContCost:int = obj["TotQuotSubContCost"]
      """  Total quoted subcontract cost for the Project phase.  """  
      self.TotQuotMtlCost:int = obj["TotQuotMtlCost"]
      """  Total quoted material cost for the Project phase.  """  
      self.TotQuotMtlBurCost:int = obj["TotQuotMtlBurCost"]
      """  Total quoted material burden cost for the Project phase.  """  
      self.Level:int = obj["Level"]
      """  This holds the bom level of the phase reletive to the parent.  """  
      self.DurationType:str = obj["DurationType"]
      """  This is will either be Hours or Days  """  
      self.RollChildMan:bool = obj["RollChildMan"]
      """  'Roll Child Manual Cost to Complete to this Level  """  
      self.RollChildBud:bool = obj["RollChildBud"]
      """  Roll Child Budgets to this Level  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Sort Sequence of the project phase.  This field controls where on the project tree the phase needs to be displayed.  """  
      self.MeasuredWorkID:str = obj["MeasuredWorkID"]
      """  Reference to the Measured Work header.  It is used to collect the cost to determine if the Measured Work was profitable or not.  """  
      self.TotQuotODCCost:int = obj["TotQuotODCCost"]
      """  Total quoted other direct cost for the Project phase.  """  
      self.ManEstCTCODCCost:int = obj["ManEstCTCODCCost"]
      """  Other direct cost manual CTC  """  
      self.TotCTCODCCost:int = obj["TotCTCODCCost"]
      """  Total calculated cost to complete other direct cost for the Project phase.  """  
      self.BudTotODCCost:int = obj["BudTotODCCost"]
      """  Other direct cost Budget Total  """  
      self.TimeApprovalsMethod:str = obj["TimeApprovalsMethod"]
      """  Defines the Approvals Method for Time related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for Time transactions related to this WBS Phase.  """  
      self.ExpenseApprovalsMethod:str = obj["ExpenseApprovalsMethod"]
      """  Defines the Approvals Method for Expenses related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for Expense transactions related to this WBS Phase.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RevMethod:str = obj["RevMethod"]
      """  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery.  """  
      self.WorkResDesc:str = obj["WorkResDesc"]
      self.StatusDesc:str = obj["StatusDesc"]
      self.GTActualCost:int = obj["GTActualCost"]
      self.GTBudgetCost:int = obj["GTBudgetCost"]
      self.GTCalculatedCost:int = obj["GTCalculatedCost"]
      self.GTEstimatedCost:int = obj["GTEstimatedCost"]
      self.GTManualCost:int = obj["GTManualCost"]
      self.GTQuotedCost:int = obj["GTQuotedCost"]
      self.createWBSJob:bool = obj["createWBSJob"]
      self.PhaseDesc:str = obj["PhaseDesc"]
      self.TimeWFGroupIDDescription:str = obj["TimeWFGroupIDDescription"]
      self.ExpenseWFGroupIDDescription:str = obj["ExpenseWFGroupIDDescription"]
      self.EnableApprovals:bool = obj["EnableApprovals"]
      self.TimeDefTaskSetID:str = obj["TimeDefTaskSetID"]
      self.ExpenseDefTaskSetID:str = obj["ExpenseDefTaskSetID"]
      self.ExpenseTaskSetDescription:str = obj["ExpenseTaskSetDescription"]
      self.TimeTaskSetDescription:str = obj["TimeTaskSetDescription"]
      self.EnableUpdOper:bool = obj["EnableUpdOper"]
      """  Flag to indicate whether the PPhaseOper for this ProjPhase should allow updates based on the status of the WBSJobNum.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      """  External field to create a WBS Phase Combo.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjPhaseListTableset:
   def __init__(self, obj):
      self.ProjPhaseList:list[Erp_Tablesets_ProjPhaseListRow] = obj["ProjPhaseList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProjPhaseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.StartDate:str = obj["StartDate"]
      """  Task start date.  """  
      self.DueDate:str = obj["DueDate"]
      """  Task due date.  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Must be greater than or equal to 0.  """  
      self.DateComplete:str = obj["DateComplete"]
      """  Date this task was complete.  """  
      self.PhaseStatus:str = obj["PhaseStatus"]
      """  Valid values are "N" = Not started, "I" = In Process, "C" = Completed.  """  
      self.Duration:int = obj["Duration"]
      """  This is the duration of the WBS Phase. On the UK software this currently uses field Number09  """  
      self.WBSJobNum:str = obj["WBSJobNum"]
      """  Reference to the job number created for the WBS Phase.  """  
      self.ParentPhase:str = obj["ParentPhase"]
      """  This is the parent phase for this WBS Phase. On the UK software this currently uses field ShortChar01  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back a alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.BudTotLbrHours:int = obj["BudTotLbrHours"]
      """  Total budget labour hours for the Project phase  """  
      self.BudTotBurHrs:int = obj["BudTotBurHrs"]
      """  Total budget burden hours for the Project phase.  """  
      self.BudTotLbrCost:int = obj["BudTotLbrCost"]
      """  Total budget labour cost for the Project phase. This is production and setup combined.  """  
      self.BudTotBurCost:int = obj["BudTotBurCost"]
      """  Total budget burden cost for the Project phase. This is production and setup combined.  """  
      self.BudTotSubCost:int = obj["BudTotSubCost"]
      """  Total budget subcontract costs for the Project phase  """  
      self.BudTotMtlCost:int = obj["BudTotMtlCost"]
      """  Total budget material costs for the Project phase  """  
      self.BudTotMtlBurCost:int = obj["BudTotMtlBurCost"]
      """  Total budget material burden costs for the Project phase.  """  
      self.TotEstLbrHrs:int = obj["TotEstLbrHrs"]
      """  Total estimated labour hours for the Project phase  """  
      self.TotEstBurdenHrs:int = obj["TotEstBurdenHrs"]
      """  Total estimated burden hours for the Project phase  """  
      self.TotEstLbrCost:int = obj["TotEstLbrCost"]
      """  Total estimated labour cost for the Project phase. This is production and setup combined.  """  
      self.TotEstSubContCost:int = obj["TotEstSubContCost"]
      """  Total estimated subcontract costs for the Project phase  """  
      self.TotEstMtlCost:int = obj["TotEstMtlCost"]
      """  Total estimated material costs for the Project phase  """  
      self.TotActLbrHrs:int = obj["TotActLbrHrs"]
      """  Total actual labour hours for the Project phase  """  
      self.TotActBurHrs:int = obj["TotActBurHrs"]
      """  Total actual burden hours for the Project phase  """  
      self.TotActLbrCost:int = obj["TotActLbrCost"]
      """  Total actual labour cost for the Project phase. This is production and setup combined.  """  
      self.TotActBurCost:int = obj["TotActBurCost"]
      """  Total actual burden cost for the Project phase. This is production and setup combined.  """  
      self.TotActSubContCost:int = obj["TotActSubContCost"]
      """  Total actual subcontract costs for the Project phase.  """  
      self.TotActMtlCost:int = obj["TotActMtlCost"]
      """  Total actual material costs for the Project phase  """  
      self.TotActMtlBurCost:int = obj["TotActMtlBurCost"]
      """  Total actual material burden costs for the Project phase.  """  
      self.ManEstCtcLbrHrs:int = obj["ManEstCtcLbrHrs"]
      """  Manually entered estimate to complete for the labour hours for the project phase  """  
      self.ManEstCtcBurHrs:int = obj["ManEstCtcBurHrs"]
      """  Manually entered estimate to complete for the burden hours.  """  
      self.ManEstCtcLbrCost:int = obj["ManEstCtcLbrCost"]
      """  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project phase.  """  
      self.ManEstCtcBurCost:int = obj["ManEstCtcBurCost"]
      """  Manually entered estimate to complete for the burden cost for the project phase.  """  
      self.ManEstCtcSubConCost:int = obj["ManEstCtcSubConCost"]
      """  Manually entered estimate to complete for the Subcontract cost for the project phase.  """  
      self.ManEstCtcMtlCost:int = obj["ManEstCtcMtlCost"]
      """  Manually entered estimate to complete for the material cost for the project phase.  """  
      self.ManEstCtcMtlBurCost:int = obj["ManEstCtcMtlBurCost"]
      """  Manually entered estimate to complete for the material burden cost for the project phase.  """  
      self.TotCtcLbrHours:int = obj["TotCtcLbrHours"]
      """  Total calculated cost to complete labour hours for the Project phase.  """  
      self.TotCtcBurHours:int = obj["TotCtcBurHours"]
      """  Total calculated cost to complete burden hours for the Project phase.  """  
      self.TotCtcLbrCost:int = obj["TotCtcLbrCost"]
      """  Total calculated cost to complete labour cost for the Project phase. This will be both production and setup.  """  
      self.TotCtcBurCost:int = obj["TotCtcBurCost"]
      """  Total calculated cost to complete burden cost for the Project phase. This will be both production and setup.  """  
      self.TotCtcSubConCost:int = obj["TotCtcSubConCost"]
      """  Total calculated cost to complete subcontract cost for the Project phase.  """  
      self.TotCtcMtlCost:int = obj["TotCtcMtlCost"]
      """  Total calculated cost to complete material cost for the Project phase.  """  
      self.TotCtcMtlBurCost:int = obj["TotCtcMtlBurCost"]
      """  Total calculated cost to complete material burden cost for the Project phase.  """  
      self.TotQuotLbrHrs:int = obj["TotQuotLbrHrs"]
      """  Total quoted labour hours for the Project phase  """  
      self.TotQuotBurHrs:int = obj["TotQuotBurHrs"]
      """  Total quoted burden hours for the Project phase.  """  
      self.TotQuotLbrCost:int = obj["TotQuotLbrCost"]
      """  Total quoted labour cost for the Project phase. This will be both production and setup.  """  
      self.TotQuotBurCost:int = obj["TotQuotBurCost"]
      """  Total quoted burden cost for the Project phase. This will be both production and setup.  """  
      self.TotQuotSubContCost:int = obj["TotQuotSubContCost"]
      """  Total quoted subcontract cost for the Project phase.  """  
      self.TotQuotMtlCost:int = obj["TotQuotMtlCost"]
      """  Total quoted material cost for the Project phase.  """  
      self.TotQuotMtlBurCost:int = obj["TotQuotMtlBurCost"]
      """  Total quoted material burden cost for the Project phase.  """  
      self.Level:int = obj["Level"]
      """  This holds the bom level of the phase reletive to the parent.  """  
      self.DurationType:str = obj["DurationType"]
      """  This is will either be Hours or Days  """  
      self.TotEstBurCost:int = obj["TotEstBurCost"]
      """  Total estimated burden cost for the Project phase. This is production and setup combined.  """  
      self.TotEstMtlBurCost:int = obj["TotEstMtlBurCost"]
      """  Total estimated material burden costs for the Project phase  """  
      self.RollChildMan:bool = obj["RollChildMan"]
      """  'Roll Child Manual Cost to Complete to this Level  """  
      self.RollChildBud:bool = obj["RollChildBud"]
      """  Roll Child Budgets to this Level  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Sort Sequence of the project phase.  This field controls where on the project tree the phase needs to be displayed.  """  
      self.MeasuredWorkID:str = obj["MeasuredWorkID"]
      """  Reference to the Measured Work header.  It is used to collect the cost to determine if the Measured Work was profitable or not.  """  
      self.TotQuotODCCost:int = obj["TotQuotODCCost"]
      """  Total quoted other direct cost for the Project phase.  """  
      self.TotEstODCCost:int = obj["TotEstODCCost"]
      """  Total estimated other direct costs for the Project phase  """  
      self.TotActODCCost:int = obj["TotActODCCost"]
      """  Total actual other direct costs for the Project phase.  """  
      self.ManEstCTCODCCost:int = obj["ManEstCTCODCCost"]
      """  Other direct cost manual CTC  """  
      self.TotCTCODCCost:int = obj["TotCTCODCCost"]
      """  Total calculated cost to complete other direct cost for the Project phase.  """  
      self.BudTotODCCost:int = obj["BudTotODCCost"]
      """  Other direct cost Budget Total  """  
      self.TimeApprovalsMethod:str = obj["TimeApprovalsMethod"]
      """  Defines the Approvals Method for Time related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for Time transactions related to this WBS Phase.  """  
      self.ExpenseApprovalsMethod:str = obj["ExpenseApprovalsMethod"]
      """  Defines the Approvals Method for Expenses related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for Expense transactions related to this WBS Phase.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvMethod:str = obj["InvMethod"]
      """  Invoicing Method  """  
      self.RevMethod:str = obj["RevMethod"]
      """  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales Order Line  """  
      self.WasRecInvoiced:bool = obj["WasRecInvoiced"]
      """  If any activity of the job assigned to the Phase has been recognized or invoiced  """  
      self.LastBuildWBSPhaseAnalysisDate:str = obj["LastBuildWBSPhaseAnalysisDate"]
      """  Date of last Build WBS Phase Analysis run.  """  
      self.PercentageOfCompletion:int = obj["PercentageOfCompletion"]
      """  Percentage of Completion  """  
      self.ToBeRecognizedLbrCost:int = obj["ToBeRecognizedLbrCost"]
      """  Labor Cost To Be Recognized  """  
      self.ToBeRecognizedBurCost:int = obj["ToBeRecognizedBurCost"]
      """  Burden Cost To Be Recognized  """  
      self.ToBeRecognizedMtlCost:int = obj["ToBeRecognizedMtlCost"]
      """  Material Cost To Be Recognized  """  
      self.ToBeRecognizedSubCost:int = obj["ToBeRecognizedSubCost"]
      """  Subcontract Cost To Be Recognized  """  
      self.ToBeRecognizedMtlBurCost:int = obj["ToBeRecognizedMtlBurCost"]
      """  Material Burden Cost To Be Recognized  """  
      self.ToBeRecognizedODCCost:int = obj["ToBeRecognizedODCCost"]
      """  ODC Cost To Be Recognized  """  
      self.ToBeRecognizedRevenue:int = obj["ToBeRecognizedRevenue"]
      """  Revenue To Be Recognized  """  
      self.RecognizeRevenueAtChildPhaseLevel:bool = obj["RecognizeRevenueAtChildPhaseLevel"]
      """  When true,  Recognize Revenue separately at Child WBS Phases.  When false, Recognize Revenue for this phase and all child phases at this level.  """  
      self.RollBudgetsToWBSPhase:bool = obj["RollBudgetsToWBSPhase"]
      """  To control if the project phase budget values are to be rolled up to the project phase.  """  
      self.TotWBSPhaseRev:int = obj["TotWBSPhaseRev"]
      """  TotWBSPhaseRev  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  The sales category code used in the Revenue recognition process.  """  
      self.ActMtlNonJobCost:int = obj["ActMtlNonJobCost"]
      """  ActMtlNonJobCost  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  AsOfDate  """  
      self.BdnRecSeqPosted:int = obj["BdnRecSeqPosted"]
      """  Number of Recalculation of burden amounts posted to GL by Revenue Recognition process  """  
      self.BdnRecSeqLastAdded:int = obj["BdnRecSeqLastAdded"]
      """  Number of Recalculation of burden amounts created by Revenue Recognition process  """  
      self.BdnRevenueAutoToday:int = obj["BdnRevenueAutoToday"]
      """  Sum of all Actual Burden Charges posted by today  """  
      self.BillingToDate:int = obj["BillingToDate"]
      """  BillingToDate  """  
      self.BuildAnalysis:bool = obj["BuildAnalysis"]
      """  BuildAnalysis  """  
      self.BurdenCostOfSales:int = obj["BurdenCostOfSales"]
      """  The burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActBurdenCost  """  
      self.BurdenLbrCstToDate:int = obj["BurdenLbrCstToDate"]
      """  BurdenLbrCstToDate  """  
      self.BurdenRecAutoCstTodate:int = obj["BurdenRecAutoCstTodate"]
      """  The burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.BurdenRecManCstTodate:int = obj["BurdenRecManCstTodate"]
      """  The burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process  """  
      self.BurManPosted:int = obj["BurManPosted"]
      """  BurManPosted  """  
      self.BurPur:int = obj["BurPur"]
      """  BurPur  """  
      self.EstBurdenCost:int = obj["EstBurdenCost"]
      """  Estimated burden cost.  """  
      self.EstBurdenHours:int = obj["EstBurdenHours"]
      """  Estimated burden hours.  """  
      self.EstLaborCost:int = obj["EstLaborCost"]
      """  Estimated labor cost.  """  
      self.EstLaborHours:int = obj["EstLaborHours"]
      """  Estimated labor hours.  """  
      self.EstMtlBurdenCost:int = obj["EstMtlBurdenCost"]
      """  Estimated material burden cost.  """  
      self.EstMtlCost:int = obj["EstMtlCost"]
      """  Estimated material cost.  """  
      self.EstODCCost:int = obj["EstODCCost"]
      """  Estimated other direct cost.  """  
      self.EstSubcontractCost:int = obj["EstSubcontractCost"]
      """  Estimated subcontract cost.  """  
      self.LaborCostOfSales:int = obj["LaborCostOfSales"]
      """  The labour costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActLaborCost.  """  
      self.LaborLbrCstToDate:int = obj["LaborLbrCstToDate"]
      """  LaborLbrCstToDate  """  
      self.LaborRecAutoCstTodate:int = obj["LaborRecAutoCstTodate"]
      """  The labour costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.LaborRecManCstTodate:int = obj["LaborRecManCstTodate"]
      """  The labor costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.LbrManPosted:int = obj["LbrManPosted"]
      """  LbrManPosted  """  
      self.LbrPur:int = obj["LbrPur"]
      """  LbrPur  """  
      self.MaterialCostOfSales:int = obj["MaterialCostOfSales"]
      """  The material costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of Material with a linesource of COS with value from ProjectAnalysis.ActMatCost.  """  
      self.MaterialRecAutoCstTodate:int = obj["MaterialRecAutoCstTodate"]
      """  The material costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.MaterialRecManCstTodate:int = obj["MaterialRecManCstTodate"]
      """  The material costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.MtlBurdenCostOfSales:int = obj["MtlBurdenCostOfSales"]
      """  The material burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActMatBurdenCost  """  
      self.MtlBurdenRecAutoCstTodate:int = obj["MtlBurdenRecAutoCstTodate"]
      """  The material burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  """  
      self.MtlBurdenRecManCstTodate:int = obj["MtlBurdenRecManCstTodate"]
      """  The material burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.MtlBurManPosted:int = obj["MtlBurManPosted"]
      """  MtlBurManPosted  """  
      self.MtlBurPur:int = obj["MtlBurPur"]
      """  MtlBurPur  """  
      self.MtlManPosted:int = obj["MtlManPosted"]
      """  MtlManPosted  """  
      self.MtlPur:int = obj["MtlPur"]
      """  MtlPur  """  
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      """  NextTmpInvcNum  """  
      self.ODCManPosted:int = obj["ODCManPosted"]
      """  ODCManPosted  """  
      self.ODCPur:int = obj["ODCPur"]
      """  ODCPur  """  
      self.ODCRecAutoCstToDate:int = obj["ODCRecAutoCstToDate"]
      """  Other Direct cost Recognition to Date  """  
      self.ODCRecManCstTodate:int = obj["ODCRecManCstTodate"]
      """  Other Direct Cost Manual Recognition to Date  """  
      self.RecManPosted:int = obj["RecManPosted"]
      """  RecManPosted  """  
      self.RecogToDtBilling:int = obj["RecogToDtBilling"]
      """  RecogToDtBilling  """  
      self.RecogToDtLbk:int = obj["RecogToDtLbk"]
      """  RecogToDtLbk  """  
      self.RecogToDtManual:int = obj["RecogToDtManual"]
      """  RecogToDtManual  """  
      self.RetentionDt:int = obj["RetentionDt"]
      """  RetentionDt  """  
      self.RevenueRecAutoToDate:int = obj["RevenueRecAutoToDate"]
      """  The revenue that has been recognised to date for the project. This is revenue that has been invoiced against the sales order either as an advanced billing or a shipment. This is the sum of ProjectAnalysis records with a Linecode of Revenue with a linesource of Invoice with value from ProjectAnalysis.ActMatCost.  """  
      self.RevenueRecManToDate:int = obj["RevenueRecManToDate"]
      """  The revenue that has been recognised to date for the project. This is revenue that has been manually recognised using this process.  """  
      self.Reverse:str = obj["Reverse"]
      """  Reverse  """  
      self.RollManEstToCpte:bool = obj["RollManEstToCpte"]
      """  RollManEstToCpte  """  
      self.SubCManPosted:int = obj["SubCManPosted"]
      """  SubCManPosted  """  
      self.SubConCostOfSales:int = obj["SubConCostOfSales"]
      """  SubConCostOfSales  """  
      self.SubConRecAutoCstTodate:int = obj["SubConRecAutoCstTodate"]
      """  SubConRecAutoCstTodate  """  
      self.SubConRecManCstTodate:int = obj["SubConRecManCstTodate"]
      """  SubConRecManCstTodate  """  
      self.SubPur:int = obj["SubPur"]
      """  SubPur  """  
      self.ConTotValue:int = obj["ConTotValue"]
      """  Total contract value for the WBS Phase.  """  
      self.DocConTotValue:int = obj["DocConTotValue"]
      """  Total contract value for the WBS Phase in the Document currency.  """  
      self.Rpt1ConTotValue:int = obj["Rpt1ConTotValue"]
      """  Total contract value for the WBS Phase in the Reporting currency.  """  
      self.Rpt2ConTotValue:int = obj["Rpt2ConTotValue"]
      """  Total contract value for the WBS Phase in the Reporting currency.  """  
      self.Rpt3ConTotValue:int = obj["Rpt3ConTotValue"]
      """  Total contract value for the WBS Phase in the Reporting currency.  """  
      self.ConTotValueNet:int = obj["ConTotValueNet"]
      """  Net total contract value for the WBS Phase.  """  
      self.DocConTotValueNet:int = obj["DocConTotValueNet"]
      """  Net total contract value for the WBS Phase in the Document currency.  """  
      self.Rpt1ConTotValueNet:int = obj["Rpt1ConTotValueNet"]
      """  Net total contract value for the WBS Phase in the Reporting currency.  """  
      self.Rpt2ConTotValueNet:int = obj["Rpt2ConTotValueNet"]
      """  Net total contract value for the WBS Phase in the Reporting currency.  """  
      self.Rpt3ConTotValueNet:int = obj["Rpt3ConTotValueNet"]
      """  Net total contract value for the WBS Phase in the Reporting currency.  """  
      self.CloseWBSJob:bool = obj["CloseWBSJob"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocBudTotBurCost:int = obj["DocBudTotBurCost"]
      self.DocBudTotLbrCost:int = obj["DocBudTotLbrCost"]
      self.DocBudTotMtlBurCost:int = obj["DocBudTotMtlBurCost"]
      self.DocBudTotMtlCost:int = obj["DocBudTotMtlCost"]
      self.DocBudTotODCCost:int = obj["DocBudTotODCCost"]
      self.DocGTActualCost:int = obj["DocGTActualCost"]
      self.DocGTBudgetCost:int = obj["DocGTBudgetCost"]
      self.DocGTCalculatedCost:int = obj["DocGTCalculatedCost"]
      self.DocGTEstimatedCost:int = obj["DocGTEstimatedCost"]
      self.DocGTManualCost:int = obj["DocGTManualCost"]
      self.DocGTQuotedCost:int = obj["DocGTQuotedCost"]
      self.DocManEstCtcBurCost:int = obj["DocManEstCtcBurCost"]
      self.DocManEstCtcLbrCost:int = obj["DocManEstCtcLbrCost"]
      self.DocManEstCtcMtlBurCost:int = obj["DocManEstCtcMtlBurCost"]
      self.DocManEstCtcMtlCost:int = obj["DocManEstCtcMtlCost"]
      self.DocManEstCTCODCCost:int = obj["DocManEstCTCODCCost"]
      self.DocManEstCtcSubConCost:int = obj["DocManEstCtcSubConCost"]
      self.DocProjectedTotalBurCost:int = obj["DocProjectedTotalBurCost"]
      self.DocProjectedTotalCost:int = obj["DocProjectedTotalCost"]
      self.DocProjectedTotalLbrCost:int = obj["DocProjectedTotalLbrCost"]
      self.DocProjectedTotalMtlBurCost:int = obj["DocProjectedTotalMtlBurCost"]
      self.DocProjectedTotalMtlCost:int = obj["DocProjectedTotalMtlCost"]
      self.DocProjectedTotalODCCost:int = obj["DocProjectedTotalODCCost"]
      self.DocProjectedTotalSubContCost:int = obj["DocProjectedTotalSubContCost"]
      self.DocTotActSubContCost:int = obj["DocTotActSubContCost"]
      self.DocTotCtcBurCost:int = obj["DocTotCtcBurCost"]
      self.DocTotCtcLbrCost:int = obj["DocTotCtcLbrCost"]
      self.DocTotCtcMtlBurCost:int = obj["DocTotCtcMtlBurCost"]
      self.DocTotCtcMtlCost:int = obj["DocTotCtcMtlCost"]
      self.DocTotCTCODCCost:int = obj["DocTotCTCODCCost"]
      self.DocTotCtcSubConCost:int = obj["DocTotCtcSubConCost"]
      self.DocTotEstBurCost:int = obj["DocTotEstBurCost"]
      self.DocTotEstLbrCost:int = obj["DocTotEstLbrCost"]
      self.DocTotEstMtlBurCost:int = obj["DocTotEstMtlBurCost"]
      self.DocTotEstMtlCost:int = obj["DocTotEstMtlCost"]
      self.DocTotEstODCCost:int = obj["DocTotEstODCCost"]
      self.DocTotEstSubContCost:int = obj["DocTotEstSubContCost"]
      self.DocTotQuotBurCost:int = obj["DocTotQuotBurCost"]
      self.DocTotQuotLbrCost:int = obj["DocTotQuotLbrCost"]
      self.DocTotQuotMtlBurCost:int = obj["DocTotQuotMtlBurCost"]
      self.DocTotQuotMtlCost:int = obj["DocTotQuotMtlCost"]
      self.DocTotQuotODCCost:int = obj["DocTotQuotODCCost"]
      self.DocTotQuotSubContCost:int = obj["DocTotQuotSubContCost"]
      self.EnableApprovals:bool = obj["EnableApprovals"]
      self.EnableRecognizeRevenueAtChildPhaseLevel:bool = obj["EnableRecognizeRevenueAtChildPhaseLevel"]
      """  This flag indicates whether ProjPhase.RecognizeRevenueAtChildPhaseLevel should be enabled in the UI.  """  
      self.EnableUpdOper:bool = obj["EnableUpdOper"]
      """  Flag to indicate whether the PPhaseOper for this ProjPhase should allow updates based on the status of the WBSJobNum.  """  
      self.EngineerWBSJob:bool = obj["EngineerWBSJob"]
      self.ExpenseDefTaskSetID:str = obj["ExpenseDefTaskSetID"]
      self.ExpenseTaskSetDescription:str = obj["ExpenseTaskSetDescription"]
      self.ExpenseWFGroupIDDescription:str = obj["ExpenseWFGroupIDDescription"]
      self.GTActualCost:int = obj["GTActualCost"]
      self.GTBudgetCost:int = obj["GTBudgetCost"]
      self.GTCalculatedCost:int = obj["GTCalculatedCost"]
      self.GTEstimatedCost:int = obj["GTEstimatedCost"]
      self.GTManualCost:int = obj["GTManualCost"]
      self.GTQuotedCost:int = obj["GTQuotedCost"]
      self.IsRootPhase:bool = obj["IsRootPhase"]
      self.JobDueDate:str = obj["JobDueDate"]
      """  used to display Due date of the WBS phase job when scheduled  """  
      self.JobStartDate:str = obj["JobStartDate"]
      """  used to display Start date of the WBS phase job when scheduled  """  
      self.ParentPhaseIsRootPhase:bool = obj["ParentPhaseIsRootPhase"]
      self.PhaseDesc:str = obj["PhaseDesc"]
      self.PInvMethod:str = obj["PInvMethod"]
      self.PRevMethod:str = obj["PRevMethod"]
      self.ProjectedTotalBurCost:int = obj["ProjectedTotalBurCost"]
      self.ProjectedTotalCost:int = obj["ProjectedTotalCost"]
      self.ProjectedTotalLbrCost:int = obj["ProjectedTotalLbrCost"]
      self.ProjectedTotalMtlBurCost:int = obj["ProjectedTotalMtlBurCost"]
      self.ProjectedTotalMtlCost:int = obj["ProjectedTotalMtlCost"]
      self.ProjectedTotalODCCost:int = obj["ProjectedTotalODCCost"]
      self.ProjectedTotalSubContCost:int = obj["ProjectedTotalSubContCost"]
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      """  External Field To create a WBS Phase Combo  """  
      self.ReleaseWBSJob:bool = obj["ReleaseWBSJob"]
      self.Rpt1BudTotBurCost:int = obj["Rpt1BudTotBurCost"]
      self.Rpt1BudTotLbrCost:int = obj["Rpt1BudTotLbrCost"]
      self.Rpt1BudTotMtlBurCost:int = obj["Rpt1BudTotMtlBurCost"]
      self.Rpt1BudTotMtlCost:int = obj["Rpt1BudTotMtlCost"]
      self.Rpt1BudTotODCCost:int = obj["Rpt1BudTotODCCost"]
      self.Rpt1BudTotSubCost:int = obj["Rpt1BudTotSubCost"]
      self.Rpt1GTActualCost:int = obj["Rpt1GTActualCost"]
      self.Rpt1GTBudgetCost:int = obj["Rpt1GTBudgetCost"]
      self.Rpt1GTCalculatedCost:int = obj["Rpt1GTCalculatedCost"]
      self.Rpt1GTEstimatedCost:int = obj["Rpt1GTEstimatedCost"]
      self.Rpt1GTManualCost:int = obj["Rpt1GTManualCost"]
      self.Rpt1GTQuotedCost:int = obj["Rpt1GTQuotedCost"]
      self.Rpt1ManEstCtcBurCost:int = obj["Rpt1ManEstCtcBurCost"]
      self.Rpt1ManEstCtcLbrCost:int = obj["Rpt1ManEstCtcLbrCost"]
      self.Rpt1ManEstCtcMtlBurCost:int = obj["Rpt1ManEstCtcMtlBurCost"]
      self.Rpt1ManEstCtcMtlCost:int = obj["Rpt1ManEstCtcMtlCost"]
      self.Rpt1ManEstCTCODCCost:int = obj["Rpt1ManEstCTCODCCost"]
      self.Rpt1ManEstCtcSubConCost:int = obj["Rpt1ManEstCtcSubConCost"]
      self.Rpt1ProjectedTotalBurCost:int = obj["Rpt1ProjectedTotalBurCost"]
      self.Rpt1ProjectedTotalCost:int = obj["Rpt1ProjectedTotalCost"]
      self.Rpt1ProjectedTotalLbrCost:int = obj["Rpt1ProjectedTotalLbrCost"]
      self.Rpt1ProjectedTotalMtlBurCost:int = obj["Rpt1ProjectedTotalMtlBurCost"]
      self.Rpt1ProjectedTotalMtlCost:int = obj["Rpt1ProjectedTotalMtlCost"]
      self.Rpt1ProjectedTotalODCCost:int = obj["Rpt1ProjectedTotalODCCost"]
      self.Rpt1ProjectedTotalSubContCost:int = obj["Rpt1ProjectedTotalSubContCost"]
      self.Rpt1TotActBurCost:int = obj["Rpt1TotActBurCost"]
      self.Rpt1TotActLbrCost:int = obj["Rpt1TotActLbrCost"]
      self.Rpt1TotActMtlBurCost:int = obj["Rpt1TotActMtlBurCost"]
      self.Rpt1TotActMtlCost:int = obj["Rpt1TotActMtlCost"]
      self.Rpt1TotActODCCost:int = obj["Rpt1TotActODCCost"]
      self.Rpt1TotActSubContCost:int = obj["Rpt1TotActSubContCost"]
      self.Rpt1TotCtcBurCost:int = obj["Rpt1TotCtcBurCost"]
      self.Rpt1TotCtcLbrCost:int = obj["Rpt1TotCtcLbrCost"]
      self.Rpt1TotCtcMtlBurCost:int = obj["Rpt1TotCtcMtlBurCost"]
      self.Rpt1TotCtcMtlCost:int = obj["Rpt1TotCtcMtlCost"]
      self.Rpt1TotCTCODCCost:int = obj["Rpt1TotCTCODCCost"]
      self.Rpt1TotCtcSubConCost:int = obj["Rpt1TotCtcSubConCost"]
      self.Rpt1TotEstBurCost:int = obj["Rpt1TotEstBurCost"]
      self.Rpt1TotEstLbrCost:int = obj["Rpt1TotEstLbrCost"]
      self.Rpt1TotEstMtlBurCost:int = obj["Rpt1TotEstMtlBurCost"]
      self.Rpt1TotEstMtlCost:int = obj["Rpt1TotEstMtlCost"]
      self.Rpt1TotEstODCCost:int = obj["Rpt1TotEstODCCost"]
      self.Rpt1TotEstSubContCost:int = obj["Rpt1TotEstSubContCost"]
      self.Rpt1TotQuotBurCost:int = obj["Rpt1TotQuotBurCost"]
      self.Rpt1TotQuotLbrCost:int = obj["Rpt1TotQuotLbrCost"]
      self.Rpt1TotQuotMtlBurCost:int = obj["Rpt1TotQuotMtlBurCost"]
      self.Rpt1TotQuotMtlCost:int = obj["Rpt1TotQuotMtlCost"]
      self.Rpt1TotQuotODCCost:int = obj["Rpt1TotQuotODCCost"]
      self.Rpt1TotQuotSubContCost:int = obj["Rpt1TotQuotSubContCost"]
      self.Rpt2BudTotBurCost:int = obj["Rpt2BudTotBurCost"]
      self.Rpt2BudTotLbrCost:int = obj["Rpt2BudTotLbrCost"]
      self.Rpt2BudTotMtlBurCost:int = obj["Rpt2BudTotMtlBurCost"]
      self.Rpt2BudTotMtlCost:int = obj["Rpt2BudTotMtlCost"]
      self.Rpt2BudTotODCCost:int = obj["Rpt2BudTotODCCost"]
      self.Rpt2BudTotSubCost:int = obj["Rpt2BudTotSubCost"]
      self.Rpt2GTActualCost:int = obj["Rpt2GTActualCost"]
      self.Rpt2GTBudgetCost:int = obj["Rpt2GTBudgetCost"]
      self.Rpt2GTCalculatedCost:int = obj["Rpt2GTCalculatedCost"]
      self.Rpt2GTEstimatedCost:int = obj["Rpt2GTEstimatedCost"]
      self.Rpt2GTManualCost:int = obj["Rpt2GTManualCost"]
      self.Rpt2GTQuotedCost:int = obj["Rpt2GTQuotedCost"]
      self.Rpt2ManEstCtcBurCost:int = obj["Rpt2ManEstCtcBurCost"]
      self.Rpt2ManEstCtcLbrCost:int = obj["Rpt2ManEstCtcLbrCost"]
      self.Rpt2ManEstCtcMtlBurCost:int = obj["Rpt2ManEstCtcMtlBurCost"]
      self.Rpt2ManEstCtcMtlCost:int = obj["Rpt2ManEstCtcMtlCost"]
      self.Rpt2ManEstCTCODCCost:int = obj["Rpt2ManEstCTCODCCost"]
      self.Rpt2ManEstCtcSubConCost:int = obj["Rpt2ManEstCtcSubConCost"]
      self.Rpt2ProjectedTotalBurCost:int = obj["Rpt2ProjectedTotalBurCost"]
      self.Rpt2ProjectedTotalCost:int = obj["Rpt2ProjectedTotalCost"]
      self.Rpt2ProjectedTotalLbrCost:int = obj["Rpt2ProjectedTotalLbrCost"]
      self.Rpt2ProjectedTotalMtlBurCost:int = obj["Rpt2ProjectedTotalMtlBurCost"]
      self.Rpt2ProjectedTotalMtlCost:int = obj["Rpt2ProjectedTotalMtlCost"]
      self.Rpt2ProjectedTotalODCCost:int = obj["Rpt2ProjectedTotalODCCost"]
      self.Rpt2ProjectedTotalSubContCost:int = obj["Rpt2ProjectedTotalSubContCost"]
      self.Rpt2TotActBurCost:int = obj["Rpt2TotActBurCost"]
      self.Rpt2TotActLbrCost:int = obj["Rpt2TotActLbrCost"]
      self.Rpt2TotActMtlBurCost:int = obj["Rpt2TotActMtlBurCost"]
      self.Rpt2TotActMtlCost:int = obj["Rpt2TotActMtlCost"]
      self.Rpt2TotActODCCost:int = obj["Rpt2TotActODCCost"]
      self.Rpt2TotActSubContCost:int = obj["Rpt2TotActSubContCost"]
      self.Rpt2TotCtcBurCost:int = obj["Rpt2TotCtcBurCost"]
      self.Rpt2TotCtcLbrCost:int = obj["Rpt2TotCtcLbrCost"]
      self.Rpt2TotCtcMtlBurCost:int = obj["Rpt2TotCtcMtlBurCost"]
      self.Rpt2TotCtcMtlCost:int = obj["Rpt2TotCtcMtlCost"]
      self.Rpt2TotCTCODCCost:int = obj["Rpt2TotCTCODCCost"]
      self.Rpt2TotCtcSubConCost:int = obj["Rpt2TotCtcSubConCost"]
      self.Rpt2TotEstBurCost:int = obj["Rpt2TotEstBurCost"]
      self.Rpt2TotEstLbrCost:int = obj["Rpt2TotEstLbrCost"]
      self.Rpt2TotEstMtlBurCost:int = obj["Rpt2TotEstMtlBurCost"]
      self.Rpt2TotEstMtlCost:int = obj["Rpt2TotEstMtlCost"]
      self.Rpt2TotEstODCCost:int = obj["Rpt2TotEstODCCost"]
      self.Rpt2TotEstSubContCost:int = obj["Rpt2TotEstSubContCost"]
      self.Rpt2TotQuotBurCost:int = obj["Rpt2TotQuotBurCost"]
      self.Rpt2TotQuotLbrCost:int = obj["Rpt2TotQuotLbrCost"]
      self.Rpt2TotQuotMtlBurCost:int = obj["Rpt2TotQuotMtlBurCost"]
      self.Rpt2TotQuotMtlCost:int = obj["Rpt2TotQuotMtlCost"]
      self.Rpt2TotQuotODCCost:int = obj["Rpt2TotQuotODCCost"]
      self.Rpt2TotQuotSubContCost:int = obj["Rpt2TotQuotSubContCost"]
      self.Rpt3BudTotBurCost:int = obj["Rpt3BudTotBurCost"]
      self.Rpt3BudTotLbrCost:int = obj["Rpt3BudTotLbrCost"]
      self.Rpt3BudTotMtlBurCost:int = obj["Rpt3BudTotMtlBurCost"]
      self.Rpt3BudTotMtlCost:int = obj["Rpt3BudTotMtlCost"]
      self.Rpt3BudTotODCCost:int = obj["Rpt3BudTotODCCost"]
      self.Rpt3BudTotSubCost:int = obj["Rpt3BudTotSubCost"]
      self.Rpt3GTActualCost:int = obj["Rpt3GTActualCost"]
      self.Rpt3GTBudgetCost:int = obj["Rpt3GTBudgetCost"]
      self.Rpt3GTCalculatedCost:int = obj["Rpt3GTCalculatedCost"]
      self.Rpt3GTEstimatedCost:int = obj["Rpt3GTEstimatedCost"]
      self.Rpt3GTManualCost:int = obj["Rpt3GTManualCost"]
      self.Rpt3GTQuotedCost:int = obj["Rpt3GTQuotedCost"]
      self.Rpt3ManEstCtcBurCost:int = obj["Rpt3ManEstCtcBurCost"]
      self.Rpt3ManEstCtcLbrCost:int = obj["Rpt3ManEstCtcLbrCost"]
      self.Rpt3ManEstCtcMtlBurCost:int = obj["Rpt3ManEstCtcMtlBurCost"]
      self.Rpt3ManEstCtcMtlCost:int = obj["Rpt3ManEstCtcMtlCost"]
      self.Rpt3ManEstCTCODCCost:int = obj["Rpt3ManEstCTCODCCost"]
      self.Rpt3ManEstCtcSubConCost:int = obj["Rpt3ManEstCtcSubConCost"]
      self.Rpt3ProjectedTotalBurCost:int = obj["Rpt3ProjectedTotalBurCost"]
      self.Rpt3ProjectedTotalCost:int = obj["Rpt3ProjectedTotalCost"]
      self.Rpt3ProjectedTotalLbrCost:int = obj["Rpt3ProjectedTotalLbrCost"]
      self.Rpt3ProjectedTotalMtlBurCost:int = obj["Rpt3ProjectedTotalMtlBurCost"]
      self.Rpt3ProjectedTotalMtlCost:int = obj["Rpt3ProjectedTotalMtlCost"]
      self.Rpt3ProjectedTotalODCCost:int = obj["Rpt3ProjectedTotalODCCost"]
      self.Rpt3ProjectedTotalSubContCost:int = obj["Rpt3ProjectedTotalSubContCost"]
      self.Rpt3TotActBurCost:int = obj["Rpt3TotActBurCost"]
      self.Rpt3TotActLbrCost:int = obj["Rpt3TotActLbrCost"]
      self.Rpt3TotActMtlBurCost:int = obj["Rpt3TotActMtlBurCost"]
      self.Rpt3TotActMtlCost:int = obj["Rpt3TotActMtlCost"]
      self.Rpt3TotActODCCost:int = obj["Rpt3TotActODCCost"]
      self.Rpt3TotActSubContCost:int = obj["Rpt3TotActSubContCost"]
      self.Rpt3TotCtcBurCost:int = obj["Rpt3TotCtcBurCost"]
      self.Rpt3TotCtcLbrCost:int = obj["Rpt3TotCtcLbrCost"]
      self.Rpt3TotCtcMtlBurCost:int = obj["Rpt3TotCtcMtlBurCost"]
      self.Rpt3TotCtcMtlCost:int = obj["Rpt3TotCtcMtlCost"]
      self.Rpt3TotCTCODCCost:int = obj["Rpt3TotCTCODCCost"]
      self.Rpt3TotCtcSubConCost:int = obj["Rpt3TotCtcSubConCost"]
      self.Rpt3TotEstBurCost:int = obj["Rpt3TotEstBurCost"]
      self.Rpt3TotEstLbrCost:int = obj["Rpt3TotEstLbrCost"]
      self.Rpt3TotEstMtlBurCost:int = obj["Rpt3TotEstMtlBurCost"]
      self.Rpt3TotEstMtlCost:int = obj["Rpt3TotEstMtlCost"]
      self.Rpt3TotEstODCCost:int = obj["Rpt3TotEstODCCost"]
      self.Rpt3TotEstSubContCost:int = obj["Rpt3TotEstSubContCost"]
      self.Rpt3TotQuotBurCost:int = obj["Rpt3TotQuotBurCost"]
      self.Rpt3TotQuotLbrCost:int = obj["Rpt3TotQuotLbrCost"]
      self.Rpt3TotQuotMtlBurCost:int = obj["Rpt3TotQuotMtlBurCost"]
      self.Rpt3TotQuotMtlCost:int = obj["Rpt3TotQuotMtlCost"]
      self.Rpt3TotQuotODCCost:int = obj["Rpt3TotQuotODCCost"]
      self.Rpt3TotQuotSubContCost:int = obj["Rpt3TotQuotSubContCost"]
      self.StatusDesc:str = obj["StatusDesc"]
      self.TimeDefTaskSetID:str = obj["TimeDefTaskSetID"]
      self.TimeTaskSetDescription:str = obj["TimeTaskSetDescription"]
      self.TimeWFGroupIDDescription:str = obj["TimeWFGroupIDDescription"]
      self.WorkResDesc:str = obj["WorkResDesc"]
      self.DocBudTotSubCost:int = obj["DocBudTotSubCost"]
      self.DocTotActBurCost:int = obj["DocTotActBurCost"]
      self.DocTotActLbrCost:int = obj["DocTotActLbrCost"]
      self.DocTotActMtlBurCost:int = obj["DocTotActMtlBurCost"]
      self.DocTotActMtlCost:int = obj["DocTotActMtlCost"]
      self.DocTotActODCCost:int = obj["DocTotActODCCost"]
      self.ExpenseApprovalTasksTree:str = obj["ExpenseApprovalTasksTree"]
      self.TimeApprovalTasksTree:str = obj["TimeApprovalTasksTree"]
      self.BitFlag:int = obj["BitFlag"]
      self.ParentPhaseDescription:str = obj["ParentPhaseDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.ProjectType_c:str = obj["ProjectType_c"]
      self.ShipToNum_c:str = obj["ShipToNum_c"]
      self.ShipToSameAsProj_c:bool = obj["ShipToSameAsProj_c"]
      self.Price_c:int = obj["Price_c"]
      self.Discount_c:int = obj["Discount_c"]
      self.ResaleRevenue_c:int = obj["ResaleRevenue_c"]
      self.FreightRevenueAmt_c:int = obj["FreightRevenueAmt_c"]
      self.SalesTaxRevenue_c:int = obj["SalesTaxRevenue_c"]
      self.Approved_c:bool = obj["Approved_c"]
      self.ApprovedBy_c:str = obj["ApprovedBy_c"]
      self.ApprovedDate_c:str = obj["ApprovedDate_c"]
      self.PartNum_c:str = obj["PartNum_c"]
      self.PartDescription_c:str = obj["PartDescription_c"]
      self.CreateRelatedPhases_c:bool = obj["CreateRelatedPhases_c"]
      pass

class Erp_Tablesets_ProjPhaseSearchTableset:
   def __init__(self, obj):
      self.ProjPhase:list[Erp_Tablesets_ProjPhaseRow] = obj["ProjPhase"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtProjPhaseSearchTableset:
   def __init__(self, obj):
      self.ProjPhase:list[Erp_Tablesets_ProjPhaseRow] = obj["ProjPhase"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   projectID
   phaseID
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      self.phaseID:str = obj["phaseID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjPhaseSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProjPhaseSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProjPhaseSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProjPhaseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewProjPhase_input:
   """ Required : 
   ds
   projectID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProjPhaseSearchTableset] = obj["ds"]
      self.projectID:str = obj["projectID"]
      pass

class GetNewProjPhase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProjPhaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseProjPhase
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseProjPhase:str = obj["whereClauseProjPhase"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjPhaseSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtProjPhaseSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtProjPhaseSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProjPhaseSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProjPhaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

