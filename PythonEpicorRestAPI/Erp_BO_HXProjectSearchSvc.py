import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.HXProjectSearchSvc
# Description: The HXProjectSearch bo.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_HXProjectSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HXProjectSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HXProjectSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HXProjectRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches",headers=creds) as resp:
           return await resp.json()

async def post_HXProjectSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HXProjectSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HXProjectRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HXProjectRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HXProjectSearches_Company_ProjectID_Revision(Company, ProjectID, Revision, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HXProjectSearch item
   Description: Calls GetByID to retrieve the HXProjectSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HXProjectSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param Revision: Desc: Revision   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HXProjectRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches(" + Company + "," + ProjectID + "," + Revision + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HXProjectSearches_Company_ProjectID_Revision(Company, ProjectID, Revision, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HXProjectSearch for the service
   Description: Calls UpdateExt to update HXProjectSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HXProjectSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param Revision: Desc: Revision   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HXProjectRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches(" + Company + "," + ProjectID + "," + Revision + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HXProjectSearches_Company_ProjectID_Revision(Company, ProjectID, Revision, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HXProjectSearch item
   Description: Call UpdateExt to delete HXProjectSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HXProjectSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param Revision: Desc: Revision   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches(" + Company + "," + ProjectID + "," + Revision + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HXProjectListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseHXProject, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseHXProject=" + whereClauseHXProject
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(projectID, revision, epicorHeaders = None):
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
   params += "projectID=" + projectID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "revision=" + revision

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHXProject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHXProject
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHXProject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHXProject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHXProject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HXProjectListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HXProjectListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HXProjectRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HXProjectRow] = obj["value"]
      pass

class Erp_Tablesets_HXProjectListRow:
   def __init__(self, obj):
      self.ActiveProject:bool = obj["ActiveProject"]
      self.BinNum:str = obj["BinNum"]
      self.CloseAccrual:bool = obj["CloseAccrual"]
      self.CommentText:str = obj["CommentText"]
      self.Company:str = obj["Company"]
      self.ConBTCustNum:int = obj["ConBTCustNum"]
      self.ConCustNum:int = obj["ConCustNum"]
      self.ConEndDate:str = obj["ConEndDate"]
      self.ConHrsInvc:str = obj["ConHrsInvc"]
      self.ConInvMeth:str = obj["ConInvMeth"]
      self.ConListCode:str = obj["ConListCode"]
      self.ConOverCeiling:bool = obj["ConOverCeiling"]
      self.ConProjectedEnd:str = obj["ConProjectedEnd"]
      self.ConProjMgr:str = obj["ConProjMgr"]
      self.ConReference:str = obj["ConReference"]
      self.ConRevMethod:str = obj["ConRevMethod"]
      self.ConStartDate:str = obj["ConStartDate"]
      self.ConTotInv:int = obj["ConTotInv"]
      self.ConTotValue:int = obj["ConTotValue"]
      self.CreatePrjJob:bool = obj["CreatePrjJob"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Description:str = obj["Description"]
      self.DocConTotInv:int = obj["DocConTotInv"]
      self.DocConTotValue:int = obj["DocConTotValue"]
      self.DocPBCeilingBur:int = obj["DocPBCeilingBur"]
      self.DocPBCeilingFees:int = obj["DocPBCeilingFees"]
      self.DocPBCeilingLbr:int = obj["DocPBCeilingLbr"]
      self.DocPBCeilingMisc:int = obj["DocPBCeilingMisc"]
      self.DocPBCeilingMtl:int = obj["DocPBCeilingMtl"]
      self.DocPBCeilingMtlBur:int = obj["DocPBCeilingMtlBur"]
      self.DocPBCeilingSub:int = obj["DocPBCeilingSub"]
      self.DocPBCeilingTotal:int = obj["DocPBCeilingTotal"]
      self.DocPBFeeLbrCharge:int = obj["DocPBFeeLbrCharge"]
      self.DocPBFeeMiscCharge:int = obj["DocPBFeeMiscCharge"]
      self.DocPBFeeMtlCharge:int = obj["DocPBFeeMtlCharge"]
      self.DocPBFeeSubCharge:int = obj["DocPBFeeSubCharge"]
      self.DocPPCeilingFees:int = obj["DocPPCeilingFees"]
      self.DocPPCeilingTotal:int = obj["DocPPCeilingTotal"]
      self.DocTotLiqToDate:int = obj["DocTotLiqToDate"]
      self.DocTotPPToDate:int = obj["DocTotPPToDate"]
      self.EndDate:str = obj["EndDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      self.LockRate:bool = obj["LockRate"]
      self.MarkUpID:str = obj["MarkUpID"]
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      self.PBBurMarkUp:int = obj["PBBurMarkUp"]
      self.PBCeilingBur:int = obj["PBCeilingBur"]
      self.PBCeilingFees:int = obj["PBCeilingFees"]
      self.PBCeilingLbr:int = obj["PBCeilingLbr"]
      self.PBCeilingMisc:int = obj["PBCeilingMisc"]
      self.PBCeilingMtl:int = obj["PBCeilingMtl"]
      self.PBCeilingMtlBur:int = obj["PBCeilingMtlBur"]
      self.PBCeilingSub:int = obj["PBCeilingSub"]
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      self.PBDocInvoicedBur:int = obj["PBDocInvoicedBur"]
      self.PBDocInvoicedFees:int = obj["PBDocInvoicedFees"]
      self.PBDocInvoicedLbr:int = obj["PBDocInvoicedLbr"]
      self.PBDocInvoicedMisc:int = obj["PBDocInvoicedMisc"]
      self.PBDocInvoicedMtl:int = obj["PBDocInvoicedMtl"]
      self.PBDocInvoicedMtlBur:int = obj["PBDocInvoicedMtlBur"]
      self.PBDocInvoicedSub:int = obj["PBDocInvoicedSub"]
      self.PBFeeApply:str = obj["PBFeeApply"]
      self.PBFeeApplyOn:str = obj["PBFeeApplyOn"]
      self.PBFeeInvoiceText:str = obj["PBFeeInvoiceText"]
      self.PBFeeLbrApply:str = obj["PBFeeLbrApply"]
      self.PBFeeLbrCharge:int = obj["PBFeeLbrCharge"]
      self.PBFeeLbrType:str = obj["PBFeeLbrType"]
      self.PBFeeMiscApply:str = obj["PBFeeMiscApply"]
      self.PBFeeMiscCharge:int = obj["PBFeeMiscCharge"]
      self.PBFeeMiscType:str = obj["PBFeeMiscType"]
      self.PBFeeMtlApply:str = obj["PBFeeMtlApply"]
      self.PBFeeMtlCharge:int = obj["PBFeeMtlCharge"]
      self.PBFeeMtlType:str = obj["PBFeeMtlType"]
      self.PBFeeProject:int = obj["PBFeeProject"]
      self.PBFeeSubApply:str = obj["PBFeeSubApply"]
      self.PBFeeSubCharge:int = obj["PBFeeSubCharge"]
      self.PBFeeSubType:str = obj["PBFeeSubType"]
      self.PBFeeType:str = obj["PBFeeType"]
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      self.PBLbMarkUp:int = obj["PBLbMarkUp"]
      self.PBMiscMarkUp:int = obj["PBMiscMarkUp"]
      self.PBMtlBurMarkUp:int = obj["PBMtlBurMarkUp"]
      self.PBMtlMarkUp:int = obj["PBMtlMarkUp"]
      self.PBOverridenMU:bool = obj["PBOverridenMU"]
      self.PBPrjRtSrc:str = obj["PBPrjRtSrc"]
      self.PBRetentionPcnt:int = obj["PBRetentionPcnt"]
      self.PBRetentionProc:str = obj["PBRetentionProc"]
      self.PBSubMarkUp:int = obj["PBSubMarkUp"]
      self.PersonList:str = obj["PersonList"]
      self.PPActive:bool = obj["PPActive"]
      self.PPAllowPcnt:int = obj["PPAllowPcnt"]
      self.PPCeilingFees:int = obj["PPCeilingFees"]
      self.PPCeilingTotal:int = obj["PPCeilingTotal"]
      self.PrimaryAsmSeq:int = obj["PrimaryAsmSeq"]
      self.PrimaryJob:str = obj["PrimaryJob"]
      self.PrimaryMtl:int = obj["PrimaryMtl"]
      self.ProdCode:str = obj["ProdCode"]
      self.ProjectID:str = obj["ProjectID"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.RetentionPrcnt:int = obj["RetentionPrcnt"]
      self.RetentionProc:str = obj["RetentionProc"]
      self.Revision:int = obj["Revision"]
      self.Rpt1ConTotInv:int = obj["Rpt1ConTotInv"]
      self.Rpt1ConTotValue:int = obj["Rpt1ConTotValue"]
      self.Rpt1PBCeilingBur:int = obj["Rpt1PBCeilingBur"]
      self.Rpt1PBCeilingFees:int = obj["Rpt1PBCeilingFees"]
      self.Rpt1PBCeilingLbr:int = obj["Rpt1PBCeilingLbr"]
      self.Rpt1PBCeilingMisc:int = obj["Rpt1PBCeilingMisc"]
      self.Rpt1PBCeilingMtl:int = obj["Rpt1PBCeilingMtl"]
      self.Rpt1PBCeilingMtlBur:int = obj["Rpt1PBCeilingMtlBur"]
      self.Rpt1PBCeilingSub:int = obj["Rpt1PBCeilingSub"]
      self.Rpt1PBCeilingTotal:int = obj["Rpt1PBCeilingTotal"]
      self.Rpt1PBFeeLbrCharge:int = obj["Rpt1PBFeeLbrCharge"]
      self.Rpt1PBFeeMiscCharge:int = obj["Rpt1PBFeeMiscCharge"]
      self.Rpt1PBFeeMtlCharge:int = obj["Rpt1PBFeeMtlCharge"]
      self.Rpt1PBFeeSubCharge:int = obj["Rpt1PBFeeSubCharge"]
      self.Rpt1PPCeilingFees:int = obj["Rpt1PPCeilingFees"]
      self.Rpt1PPCeilingTotal:int = obj["Rpt1PPCeilingTotal"]
      self.Rpt1TotLiqToDate:int = obj["Rpt1TotLiqToDate"]
      self.Rpt1TotPPToDate:int = obj["Rpt1TotPPToDate"]
      self.Rpt2ConTotInv:int = obj["Rpt2ConTotInv"]
      self.Rpt2ConTotValue:int = obj["Rpt2ConTotValue"]
      self.Rpt2PBCeilingBur:int = obj["Rpt2PBCeilingBur"]
      self.Rpt2PBCeilingFees:int = obj["Rpt2PBCeilingFees"]
      self.Rpt2PBCeilingLbr:int = obj["Rpt2PBCeilingLbr"]
      self.Rpt2PBCeilingMisc:int = obj["Rpt2PBCeilingMisc"]
      self.Rpt2PBCeilingMtl:int = obj["Rpt2PBCeilingMtl"]
      self.Rpt2PBCeilingMtlBur:int = obj["Rpt2PBCeilingMtlBur"]
      self.Rpt2PBCeilingSub:int = obj["Rpt2PBCeilingSub"]
      self.Rpt2PBCeilingTotal:int = obj["Rpt2PBCeilingTotal"]
      self.Rpt2PBFeeLbrCharge:int = obj["Rpt2PBFeeLbrCharge"]
      self.Rpt2PBFeeMiscCharge:int = obj["Rpt2PBFeeMiscCharge"]
      self.Rpt2PBFeeMtlCharge:int = obj["Rpt2PBFeeMtlCharge"]
      self.Rpt2PBFeeSubCharge:int = obj["Rpt2PBFeeSubCharge"]
      self.Rpt2PPCeilingFees:int = obj["Rpt2PPCeilingFees"]
      self.Rpt2PPCeilingTotal:int = obj["Rpt2PPCeilingTotal"]
      self.Rpt2TotLiqToDate:int = obj["Rpt2TotLiqToDate"]
      self.Rpt2TotPPToDate:int = obj["Rpt2TotPPToDate"]
      self.Rpt3ConTotInv:int = obj["Rpt3ConTotInv"]
      self.Rpt3ConTotValue:int = obj["Rpt3ConTotValue"]
      self.Rpt3PBCeilingBur:int = obj["Rpt3PBCeilingBur"]
      self.Rpt3PBCeilingFees:int = obj["Rpt3PBCeilingFees"]
      self.Rpt3PBCeilingLbr:int = obj["Rpt3PBCeilingLbr"]
      self.Rpt3PBCeilingMisc:int = obj["Rpt3PBCeilingMisc"]
      self.Rpt3PBCeilingMtl:int = obj["Rpt3PBCeilingMtl"]
      self.Rpt3PBCeilingMtlBur:int = obj["Rpt3PBCeilingMtlBur"]
      self.Rpt3PBCeilingSub:int = obj["Rpt3PBCeilingSub"]
      self.Rpt3PBCeilingTotal:int = obj["Rpt3PBCeilingTotal"]
      self.Rpt3PBFeeLbrCharge:int = obj["Rpt3PBFeeLbrCharge"]
      self.Rpt3PBFeeMiscCharge:int = obj["Rpt3PBFeeMiscCharge"]
      self.Rpt3PBFeeMtlCharge:int = obj["Rpt3PBFeeMtlCharge"]
      self.Rpt3PBFeeSubCharge:int = obj["Rpt3PBFeeSubCharge"]
      self.Rpt3PPCeilingFees:int = obj["Rpt3PPCeilingFees"]
      self.Rpt3PPCeilingTotal:int = obj["Rpt3PPCeilingTotal"]
      self.Rpt3TotLiqToDate:int = obj["Rpt3TotLiqToDate"]
      self.Rpt3TotPPToDate:int = obj["Rpt3TotPPToDate"]
      self.SalesCatID:str = obj["SalesCatID"]
      self.StartDate:str = obj["StartDate"]
      self.TotLiqToDate:int = obj["TotLiqToDate"]
      self.TotPPToDate:int = obj["TotPPToDate"]
      self.UserMap:str = obj["UserMap"]
      self.UserMapData:str = obj["UserMapData"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.MtlTaxCatID:str = obj["MtlTaxCatID"]
      self.LbrTaxCatID:str = obj["LbrTaxCatID"]
      self.FeeTaxCatID:str = obj["FeeTaxCatID"]
      self.ODCTaxCatID:str = obj["ODCTaxCatID"]
      self.SubTaxCatID:str = obj["SubTaxCatID"]
      self.BdnTaxCatID:str = obj["BdnTaxCatID"]
      self.RetTaxCatID:str = obj["RetTaxCatID"]
      self.TaxOnNetOfRet:bool = obj["TaxOnNetOfRet"]
      self.CeilTaxCatID:str = obj["CeilTaxCatID"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HXProjectRow:
   def __init__(self, obj):
      self.ActiveProject:bool = obj["ActiveProject"]
      self.BinNum:str = obj["BinNum"]
      self.CloseAccrual:bool = obj["CloseAccrual"]
      self.CommentText:str = obj["CommentText"]
      self.Company:str = obj["Company"]
      self.ConBTCustNum:int = obj["ConBTCustNum"]
      self.ConCustNum:int = obj["ConCustNum"]
      self.ConEndDate:str = obj["ConEndDate"]
      self.ConHrsInvc:str = obj["ConHrsInvc"]
      self.ConInvMeth:str = obj["ConInvMeth"]
      self.ConListCode:str = obj["ConListCode"]
      self.ConOverCeiling:bool = obj["ConOverCeiling"]
      self.ConProjectedEnd:str = obj["ConProjectedEnd"]
      self.ConProjMgr:str = obj["ConProjMgr"]
      self.ConReference:str = obj["ConReference"]
      self.ConRevMethod:str = obj["ConRevMethod"]
      self.ConStartDate:str = obj["ConStartDate"]
      self.ConTotInv:int = obj["ConTotInv"]
      self.ConTotValue:int = obj["ConTotValue"]
      self.CreatePrjJob:bool = obj["CreatePrjJob"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Description:str = obj["Description"]
      self.DocConTotInv:int = obj["DocConTotInv"]
      self.DocConTotValue:int = obj["DocConTotValue"]
      self.DocPBCeilingBur:int = obj["DocPBCeilingBur"]
      self.DocPBCeilingFees:int = obj["DocPBCeilingFees"]
      self.DocPBCeilingLbr:int = obj["DocPBCeilingLbr"]
      self.DocPBCeilingMisc:int = obj["DocPBCeilingMisc"]
      self.DocPBCeilingMtl:int = obj["DocPBCeilingMtl"]
      self.DocPBCeilingMtlBur:int = obj["DocPBCeilingMtlBur"]
      self.DocPBCeilingSub:int = obj["DocPBCeilingSub"]
      self.DocPBCeilingTotal:int = obj["DocPBCeilingTotal"]
      self.DocPBFeeLbrCharge:int = obj["DocPBFeeLbrCharge"]
      self.DocPBFeeMiscCharge:int = obj["DocPBFeeMiscCharge"]
      self.DocPBFeeMtlCharge:int = obj["DocPBFeeMtlCharge"]
      self.DocPBFeeSubCharge:int = obj["DocPBFeeSubCharge"]
      self.DocPPCeilingFees:int = obj["DocPPCeilingFees"]
      self.DocPPCeilingTotal:int = obj["DocPPCeilingTotal"]
      self.DocTotLiqToDate:int = obj["DocTotLiqToDate"]
      self.DocTotPPToDate:int = obj["DocTotPPToDate"]
      self.EndDate:str = obj["EndDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      self.LockRate:bool = obj["LockRate"]
      self.MarkUpID:str = obj["MarkUpID"]
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      self.PBBurMarkUp:int = obj["PBBurMarkUp"]
      self.PBCeilingBur:int = obj["PBCeilingBur"]
      self.PBCeilingFees:int = obj["PBCeilingFees"]
      self.PBCeilingLbr:int = obj["PBCeilingLbr"]
      self.PBCeilingMisc:int = obj["PBCeilingMisc"]
      self.PBCeilingMtl:int = obj["PBCeilingMtl"]
      self.PBCeilingMtlBur:int = obj["PBCeilingMtlBur"]
      self.PBCeilingSub:int = obj["PBCeilingSub"]
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      self.PBDocInvoicedBur:int = obj["PBDocInvoicedBur"]
      self.PBDocInvoicedFees:int = obj["PBDocInvoicedFees"]
      self.PBDocInvoicedLbr:int = obj["PBDocInvoicedLbr"]
      self.PBDocInvoicedMisc:int = obj["PBDocInvoicedMisc"]
      self.PBDocInvoicedMtl:int = obj["PBDocInvoicedMtl"]
      self.PBDocInvoicedMtlBur:int = obj["PBDocInvoicedMtlBur"]
      self.PBDocInvoicedSub:int = obj["PBDocInvoicedSub"]
      self.PBFeeApply:str = obj["PBFeeApply"]
      self.PBFeeApplyOn:str = obj["PBFeeApplyOn"]
      self.PBFeeInvoiceText:str = obj["PBFeeInvoiceText"]
      self.PBFeeLbrApply:str = obj["PBFeeLbrApply"]
      self.PBFeeLbrCharge:int = obj["PBFeeLbrCharge"]
      self.PBFeeLbrType:str = obj["PBFeeLbrType"]
      self.PBFeeMiscApply:str = obj["PBFeeMiscApply"]
      self.PBFeeMiscCharge:int = obj["PBFeeMiscCharge"]
      self.PBFeeMiscType:str = obj["PBFeeMiscType"]
      self.PBFeeMtlApply:str = obj["PBFeeMtlApply"]
      self.PBFeeMtlCharge:int = obj["PBFeeMtlCharge"]
      self.PBFeeMtlType:str = obj["PBFeeMtlType"]
      self.PBFeeProject:int = obj["PBFeeProject"]
      self.PBFeeSubApply:str = obj["PBFeeSubApply"]
      self.PBFeeSubCharge:int = obj["PBFeeSubCharge"]
      self.PBFeeSubType:str = obj["PBFeeSubType"]
      self.PBFeeType:str = obj["PBFeeType"]
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      self.PBLbMarkUp:int = obj["PBLbMarkUp"]
      self.PBMiscMarkUp:int = obj["PBMiscMarkUp"]
      self.PBMtlBurMarkUp:int = obj["PBMtlBurMarkUp"]
      self.PBMtlMarkUp:int = obj["PBMtlMarkUp"]
      self.PBOverridenMU:bool = obj["PBOverridenMU"]
      self.PBPrjRtSrc:str = obj["PBPrjRtSrc"]
      self.PBRetentionPcnt:int = obj["PBRetentionPcnt"]
      self.PBRetentionProc:str = obj["PBRetentionProc"]
      self.PBSubMarkUp:int = obj["PBSubMarkUp"]
      self.PersonList:str = obj["PersonList"]
      self.PPActive:bool = obj["PPActive"]
      self.PPAllowPcnt:int = obj["PPAllowPcnt"]
      self.PPCeilingFees:int = obj["PPCeilingFees"]
      self.PPCeilingTotal:int = obj["PPCeilingTotal"]
      self.PrimaryAsmSeq:int = obj["PrimaryAsmSeq"]
      self.PrimaryJob:str = obj["PrimaryJob"]
      self.PrimaryMtl:int = obj["PrimaryMtl"]
      self.ProdCode:str = obj["ProdCode"]
      self.ProjectID:str = obj["ProjectID"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.RetentionPrcnt:int = obj["RetentionPrcnt"]
      self.RetentionProc:str = obj["RetentionProc"]
      self.Revision:int = obj["Revision"]
      self.Rpt1ConTotInv:int = obj["Rpt1ConTotInv"]
      self.Rpt1ConTotValue:int = obj["Rpt1ConTotValue"]
      self.Rpt1PBCeilingBur:int = obj["Rpt1PBCeilingBur"]
      self.Rpt1PBCeilingFees:int = obj["Rpt1PBCeilingFees"]
      self.Rpt1PBCeilingLbr:int = obj["Rpt1PBCeilingLbr"]
      self.Rpt1PBCeilingMisc:int = obj["Rpt1PBCeilingMisc"]
      self.Rpt1PBCeilingMtl:int = obj["Rpt1PBCeilingMtl"]
      self.Rpt1PBCeilingMtlBur:int = obj["Rpt1PBCeilingMtlBur"]
      self.Rpt1PBCeilingSub:int = obj["Rpt1PBCeilingSub"]
      self.Rpt1PBCeilingTotal:int = obj["Rpt1PBCeilingTotal"]
      self.Rpt1PBFeeLbrCharge:int = obj["Rpt1PBFeeLbrCharge"]
      self.Rpt1PBFeeMiscCharge:int = obj["Rpt1PBFeeMiscCharge"]
      self.Rpt1PBFeeMtlCharge:int = obj["Rpt1PBFeeMtlCharge"]
      self.Rpt1PBFeeSubCharge:int = obj["Rpt1PBFeeSubCharge"]
      self.Rpt1PPCeilingFees:int = obj["Rpt1PPCeilingFees"]
      self.Rpt1PPCeilingTotal:int = obj["Rpt1PPCeilingTotal"]
      self.Rpt1TotLiqToDate:int = obj["Rpt1TotLiqToDate"]
      self.Rpt1TotPPToDate:int = obj["Rpt1TotPPToDate"]
      self.Rpt2ConTotInv:int = obj["Rpt2ConTotInv"]
      self.Rpt2ConTotValue:int = obj["Rpt2ConTotValue"]
      self.Rpt2PBCeilingBur:int = obj["Rpt2PBCeilingBur"]
      self.Rpt2PBCeilingFees:int = obj["Rpt2PBCeilingFees"]
      self.Rpt2PBCeilingLbr:int = obj["Rpt2PBCeilingLbr"]
      self.Rpt2PBCeilingMisc:int = obj["Rpt2PBCeilingMisc"]
      self.Rpt2PBCeilingMtl:int = obj["Rpt2PBCeilingMtl"]
      self.Rpt2PBCeilingMtlBur:int = obj["Rpt2PBCeilingMtlBur"]
      self.Rpt2PBCeilingSub:int = obj["Rpt2PBCeilingSub"]
      self.Rpt2PBCeilingTotal:int = obj["Rpt2PBCeilingTotal"]
      self.Rpt2PBFeeLbrCharge:int = obj["Rpt2PBFeeLbrCharge"]
      self.Rpt2PBFeeMiscCharge:int = obj["Rpt2PBFeeMiscCharge"]
      self.Rpt2PBFeeMtlCharge:int = obj["Rpt2PBFeeMtlCharge"]
      self.Rpt2PBFeeSubCharge:int = obj["Rpt2PBFeeSubCharge"]
      self.Rpt2PPCeilingFees:int = obj["Rpt2PPCeilingFees"]
      self.Rpt2PPCeilingTotal:int = obj["Rpt2PPCeilingTotal"]
      self.Rpt2TotLiqToDate:int = obj["Rpt2TotLiqToDate"]
      self.Rpt2TotPPToDate:int = obj["Rpt2TotPPToDate"]
      self.Rpt3ConTotInv:int = obj["Rpt3ConTotInv"]
      self.Rpt3ConTotValue:int = obj["Rpt3ConTotValue"]
      self.Rpt3PBCeilingBur:int = obj["Rpt3PBCeilingBur"]
      self.Rpt3PBCeilingFees:int = obj["Rpt3PBCeilingFees"]
      self.Rpt3PBCeilingLbr:int = obj["Rpt3PBCeilingLbr"]
      self.Rpt3PBCeilingMisc:int = obj["Rpt3PBCeilingMisc"]
      self.Rpt3PBCeilingMtl:int = obj["Rpt3PBCeilingMtl"]
      self.Rpt3PBCeilingMtlBur:int = obj["Rpt3PBCeilingMtlBur"]
      self.Rpt3PBCeilingSub:int = obj["Rpt3PBCeilingSub"]
      self.Rpt3PBCeilingTotal:int = obj["Rpt3PBCeilingTotal"]
      self.Rpt3PBFeeLbrCharge:int = obj["Rpt3PBFeeLbrCharge"]
      self.Rpt3PBFeeMiscCharge:int = obj["Rpt3PBFeeMiscCharge"]
      self.Rpt3PBFeeMtlCharge:int = obj["Rpt3PBFeeMtlCharge"]
      self.Rpt3PBFeeSubCharge:int = obj["Rpt3PBFeeSubCharge"]
      self.Rpt3PPCeilingFees:int = obj["Rpt3PPCeilingFees"]
      self.Rpt3PPCeilingTotal:int = obj["Rpt3PPCeilingTotal"]
      self.Rpt3TotLiqToDate:int = obj["Rpt3TotLiqToDate"]
      self.Rpt3TotPPToDate:int = obj["Rpt3TotPPToDate"]
      self.SalesCatID:str = obj["SalesCatID"]
      self.StartDate:str = obj["StartDate"]
      self.TotLiqToDate:int = obj["TotLiqToDate"]
      self.TotPPToDate:int = obj["TotPPToDate"]
      self.UserMap:str = obj["UserMap"]
      self.UserMapData:str = obj["UserMapData"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.MtlTaxCatID:str = obj["MtlTaxCatID"]
      self.LbrTaxCatID:str = obj["LbrTaxCatID"]
      self.FeeTaxCatID:str = obj["FeeTaxCatID"]
      self.ODCTaxCatID:str = obj["ODCTaxCatID"]
      self.SubTaxCatID:str = obj["SubTaxCatID"]
      self.BdnTaxCatID:str = obj["BdnTaxCatID"]
      self.RetTaxCatID:str = obj["RetTaxCatID"]
      self.TaxOnNetOfRet:bool = obj["TaxOnNetOfRet"]
      self.CeilTaxCatID:str = obj["CeilTaxCatID"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LastAction:str = obj["LastAction"]
      """  LastAction  """  
      self.ActionDate:str = obj["ActionDate"]
      """  ActionDate  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   projectID
   revision
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      self.revision:int = obj["revision"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_HXProjectListRow:
   def __init__(self, obj):
      self.ActiveProject:bool = obj["ActiveProject"]
      self.BinNum:str = obj["BinNum"]
      self.CloseAccrual:bool = obj["CloseAccrual"]
      self.CommentText:str = obj["CommentText"]
      self.Company:str = obj["Company"]
      self.ConBTCustNum:int = obj["ConBTCustNum"]
      self.ConCustNum:int = obj["ConCustNum"]
      self.ConEndDate:str = obj["ConEndDate"]
      self.ConHrsInvc:str = obj["ConHrsInvc"]
      self.ConInvMeth:str = obj["ConInvMeth"]
      self.ConListCode:str = obj["ConListCode"]
      self.ConOverCeiling:bool = obj["ConOverCeiling"]
      self.ConProjectedEnd:str = obj["ConProjectedEnd"]
      self.ConProjMgr:str = obj["ConProjMgr"]
      self.ConReference:str = obj["ConReference"]
      self.ConRevMethod:str = obj["ConRevMethod"]
      self.ConStartDate:str = obj["ConStartDate"]
      self.ConTotInv:int = obj["ConTotInv"]
      self.ConTotValue:int = obj["ConTotValue"]
      self.CreatePrjJob:bool = obj["CreatePrjJob"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Description:str = obj["Description"]
      self.DocConTotInv:int = obj["DocConTotInv"]
      self.DocConTotValue:int = obj["DocConTotValue"]
      self.DocPBCeilingBur:int = obj["DocPBCeilingBur"]
      self.DocPBCeilingFees:int = obj["DocPBCeilingFees"]
      self.DocPBCeilingLbr:int = obj["DocPBCeilingLbr"]
      self.DocPBCeilingMisc:int = obj["DocPBCeilingMisc"]
      self.DocPBCeilingMtl:int = obj["DocPBCeilingMtl"]
      self.DocPBCeilingMtlBur:int = obj["DocPBCeilingMtlBur"]
      self.DocPBCeilingSub:int = obj["DocPBCeilingSub"]
      self.DocPBCeilingTotal:int = obj["DocPBCeilingTotal"]
      self.DocPBFeeLbrCharge:int = obj["DocPBFeeLbrCharge"]
      self.DocPBFeeMiscCharge:int = obj["DocPBFeeMiscCharge"]
      self.DocPBFeeMtlCharge:int = obj["DocPBFeeMtlCharge"]
      self.DocPBFeeSubCharge:int = obj["DocPBFeeSubCharge"]
      self.DocPPCeilingFees:int = obj["DocPPCeilingFees"]
      self.DocPPCeilingTotal:int = obj["DocPPCeilingTotal"]
      self.DocTotLiqToDate:int = obj["DocTotLiqToDate"]
      self.DocTotPPToDate:int = obj["DocTotPPToDate"]
      self.EndDate:str = obj["EndDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      self.LockRate:bool = obj["LockRate"]
      self.MarkUpID:str = obj["MarkUpID"]
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      self.PBBurMarkUp:int = obj["PBBurMarkUp"]
      self.PBCeilingBur:int = obj["PBCeilingBur"]
      self.PBCeilingFees:int = obj["PBCeilingFees"]
      self.PBCeilingLbr:int = obj["PBCeilingLbr"]
      self.PBCeilingMisc:int = obj["PBCeilingMisc"]
      self.PBCeilingMtl:int = obj["PBCeilingMtl"]
      self.PBCeilingMtlBur:int = obj["PBCeilingMtlBur"]
      self.PBCeilingSub:int = obj["PBCeilingSub"]
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      self.PBDocInvoicedBur:int = obj["PBDocInvoicedBur"]
      self.PBDocInvoicedFees:int = obj["PBDocInvoicedFees"]
      self.PBDocInvoicedLbr:int = obj["PBDocInvoicedLbr"]
      self.PBDocInvoicedMisc:int = obj["PBDocInvoicedMisc"]
      self.PBDocInvoicedMtl:int = obj["PBDocInvoicedMtl"]
      self.PBDocInvoicedMtlBur:int = obj["PBDocInvoicedMtlBur"]
      self.PBDocInvoicedSub:int = obj["PBDocInvoicedSub"]
      self.PBFeeApply:str = obj["PBFeeApply"]
      self.PBFeeApplyOn:str = obj["PBFeeApplyOn"]
      self.PBFeeInvoiceText:str = obj["PBFeeInvoiceText"]
      self.PBFeeLbrApply:str = obj["PBFeeLbrApply"]
      self.PBFeeLbrCharge:int = obj["PBFeeLbrCharge"]
      self.PBFeeLbrType:str = obj["PBFeeLbrType"]
      self.PBFeeMiscApply:str = obj["PBFeeMiscApply"]
      self.PBFeeMiscCharge:int = obj["PBFeeMiscCharge"]
      self.PBFeeMiscType:str = obj["PBFeeMiscType"]
      self.PBFeeMtlApply:str = obj["PBFeeMtlApply"]
      self.PBFeeMtlCharge:int = obj["PBFeeMtlCharge"]
      self.PBFeeMtlType:str = obj["PBFeeMtlType"]
      self.PBFeeProject:int = obj["PBFeeProject"]
      self.PBFeeSubApply:str = obj["PBFeeSubApply"]
      self.PBFeeSubCharge:int = obj["PBFeeSubCharge"]
      self.PBFeeSubType:str = obj["PBFeeSubType"]
      self.PBFeeType:str = obj["PBFeeType"]
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      self.PBLbMarkUp:int = obj["PBLbMarkUp"]
      self.PBMiscMarkUp:int = obj["PBMiscMarkUp"]
      self.PBMtlBurMarkUp:int = obj["PBMtlBurMarkUp"]
      self.PBMtlMarkUp:int = obj["PBMtlMarkUp"]
      self.PBOverridenMU:bool = obj["PBOverridenMU"]
      self.PBPrjRtSrc:str = obj["PBPrjRtSrc"]
      self.PBRetentionPcnt:int = obj["PBRetentionPcnt"]
      self.PBRetentionProc:str = obj["PBRetentionProc"]
      self.PBSubMarkUp:int = obj["PBSubMarkUp"]
      self.PersonList:str = obj["PersonList"]
      self.PPActive:bool = obj["PPActive"]
      self.PPAllowPcnt:int = obj["PPAllowPcnt"]
      self.PPCeilingFees:int = obj["PPCeilingFees"]
      self.PPCeilingTotal:int = obj["PPCeilingTotal"]
      self.PrimaryAsmSeq:int = obj["PrimaryAsmSeq"]
      self.PrimaryJob:str = obj["PrimaryJob"]
      self.PrimaryMtl:int = obj["PrimaryMtl"]
      self.ProdCode:str = obj["ProdCode"]
      self.ProjectID:str = obj["ProjectID"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.RetentionPrcnt:int = obj["RetentionPrcnt"]
      self.RetentionProc:str = obj["RetentionProc"]
      self.Revision:int = obj["Revision"]
      self.Rpt1ConTotInv:int = obj["Rpt1ConTotInv"]
      self.Rpt1ConTotValue:int = obj["Rpt1ConTotValue"]
      self.Rpt1PBCeilingBur:int = obj["Rpt1PBCeilingBur"]
      self.Rpt1PBCeilingFees:int = obj["Rpt1PBCeilingFees"]
      self.Rpt1PBCeilingLbr:int = obj["Rpt1PBCeilingLbr"]
      self.Rpt1PBCeilingMisc:int = obj["Rpt1PBCeilingMisc"]
      self.Rpt1PBCeilingMtl:int = obj["Rpt1PBCeilingMtl"]
      self.Rpt1PBCeilingMtlBur:int = obj["Rpt1PBCeilingMtlBur"]
      self.Rpt1PBCeilingSub:int = obj["Rpt1PBCeilingSub"]
      self.Rpt1PBCeilingTotal:int = obj["Rpt1PBCeilingTotal"]
      self.Rpt1PBFeeLbrCharge:int = obj["Rpt1PBFeeLbrCharge"]
      self.Rpt1PBFeeMiscCharge:int = obj["Rpt1PBFeeMiscCharge"]
      self.Rpt1PBFeeMtlCharge:int = obj["Rpt1PBFeeMtlCharge"]
      self.Rpt1PBFeeSubCharge:int = obj["Rpt1PBFeeSubCharge"]
      self.Rpt1PPCeilingFees:int = obj["Rpt1PPCeilingFees"]
      self.Rpt1PPCeilingTotal:int = obj["Rpt1PPCeilingTotal"]
      self.Rpt1TotLiqToDate:int = obj["Rpt1TotLiqToDate"]
      self.Rpt1TotPPToDate:int = obj["Rpt1TotPPToDate"]
      self.Rpt2ConTotInv:int = obj["Rpt2ConTotInv"]
      self.Rpt2ConTotValue:int = obj["Rpt2ConTotValue"]
      self.Rpt2PBCeilingBur:int = obj["Rpt2PBCeilingBur"]
      self.Rpt2PBCeilingFees:int = obj["Rpt2PBCeilingFees"]
      self.Rpt2PBCeilingLbr:int = obj["Rpt2PBCeilingLbr"]
      self.Rpt2PBCeilingMisc:int = obj["Rpt2PBCeilingMisc"]
      self.Rpt2PBCeilingMtl:int = obj["Rpt2PBCeilingMtl"]
      self.Rpt2PBCeilingMtlBur:int = obj["Rpt2PBCeilingMtlBur"]
      self.Rpt2PBCeilingSub:int = obj["Rpt2PBCeilingSub"]
      self.Rpt2PBCeilingTotal:int = obj["Rpt2PBCeilingTotal"]
      self.Rpt2PBFeeLbrCharge:int = obj["Rpt2PBFeeLbrCharge"]
      self.Rpt2PBFeeMiscCharge:int = obj["Rpt2PBFeeMiscCharge"]
      self.Rpt2PBFeeMtlCharge:int = obj["Rpt2PBFeeMtlCharge"]
      self.Rpt2PBFeeSubCharge:int = obj["Rpt2PBFeeSubCharge"]
      self.Rpt2PPCeilingFees:int = obj["Rpt2PPCeilingFees"]
      self.Rpt2PPCeilingTotal:int = obj["Rpt2PPCeilingTotal"]
      self.Rpt2TotLiqToDate:int = obj["Rpt2TotLiqToDate"]
      self.Rpt2TotPPToDate:int = obj["Rpt2TotPPToDate"]
      self.Rpt3ConTotInv:int = obj["Rpt3ConTotInv"]
      self.Rpt3ConTotValue:int = obj["Rpt3ConTotValue"]
      self.Rpt3PBCeilingBur:int = obj["Rpt3PBCeilingBur"]
      self.Rpt3PBCeilingFees:int = obj["Rpt3PBCeilingFees"]
      self.Rpt3PBCeilingLbr:int = obj["Rpt3PBCeilingLbr"]
      self.Rpt3PBCeilingMisc:int = obj["Rpt3PBCeilingMisc"]
      self.Rpt3PBCeilingMtl:int = obj["Rpt3PBCeilingMtl"]
      self.Rpt3PBCeilingMtlBur:int = obj["Rpt3PBCeilingMtlBur"]
      self.Rpt3PBCeilingSub:int = obj["Rpt3PBCeilingSub"]
      self.Rpt3PBCeilingTotal:int = obj["Rpt3PBCeilingTotal"]
      self.Rpt3PBFeeLbrCharge:int = obj["Rpt3PBFeeLbrCharge"]
      self.Rpt3PBFeeMiscCharge:int = obj["Rpt3PBFeeMiscCharge"]
      self.Rpt3PBFeeMtlCharge:int = obj["Rpt3PBFeeMtlCharge"]
      self.Rpt3PBFeeSubCharge:int = obj["Rpt3PBFeeSubCharge"]
      self.Rpt3PPCeilingFees:int = obj["Rpt3PPCeilingFees"]
      self.Rpt3PPCeilingTotal:int = obj["Rpt3PPCeilingTotal"]
      self.Rpt3TotLiqToDate:int = obj["Rpt3TotLiqToDate"]
      self.Rpt3TotPPToDate:int = obj["Rpt3TotPPToDate"]
      self.SalesCatID:str = obj["SalesCatID"]
      self.StartDate:str = obj["StartDate"]
      self.TotLiqToDate:int = obj["TotLiqToDate"]
      self.TotPPToDate:int = obj["TotPPToDate"]
      self.UserMap:str = obj["UserMap"]
      self.UserMapData:str = obj["UserMapData"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.MtlTaxCatID:str = obj["MtlTaxCatID"]
      self.LbrTaxCatID:str = obj["LbrTaxCatID"]
      self.FeeTaxCatID:str = obj["FeeTaxCatID"]
      self.ODCTaxCatID:str = obj["ODCTaxCatID"]
      self.SubTaxCatID:str = obj["SubTaxCatID"]
      self.BdnTaxCatID:str = obj["BdnTaxCatID"]
      self.RetTaxCatID:str = obj["RetTaxCatID"]
      self.TaxOnNetOfRet:bool = obj["TaxOnNetOfRet"]
      self.CeilTaxCatID:str = obj["CeilTaxCatID"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HXProjectListTableset:
   def __init__(self, obj):
      self.HXProjectList:list[Erp_Tablesets_HXProjectListRow] = obj["HXProjectList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_HXProjectRow:
   def __init__(self, obj):
      self.ActiveProject:bool = obj["ActiveProject"]
      self.BinNum:str = obj["BinNum"]
      self.CloseAccrual:bool = obj["CloseAccrual"]
      self.CommentText:str = obj["CommentText"]
      self.Company:str = obj["Company"]
      self.ConBTCustNum:int = obj["ConBTCustNum"]
      self.ConCustNum:int = obj["ConCustNum"]
      self.ConEndDate:str = obj["ConEndDate"]
      self.ConHrsInvc:str = obj["ConHrsInvc"]
      self.ConInvMeth:str = obj["ConInvMeth"]
      self.ConListCode:str = obj["ConListCode"]
      self.ConOverCeiling:bool = obj["ConOverCeiling"]
      self.ConProjectedEnd:str = obj["ConProjectedEnd"]
      self.ConProjMgr:str = obj["ConProjMgr"]
      self.ConReference:str = obj["ConReference"]
      self.ConRevMethod:str = obj["ConRevMethod"]
      self.ConStartDate:str = obj["ConStartDate"]
      self.ConTotInv:int = obj["ConTotInv"]
      self.ConTotValue:int = obj["ConTotValue"]
      self.CreatePrjJob:bool = obj["CreatePrjJob"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Description:str = obj["Description"]
      self.DocConTotInv:int = obj["DocConTotInv"]
      self.DocConTotValue:int = obj["DocConTotValue"]
      self.DocPBCeilingBur:int = obj["DocPBCeilingBur"]
      self.DocPBCeilingFees:int = obj["DocPBCeilingFees"]
      self.DocPBCeilingLbr:int = obj["DocPBCeilingLbr"]
      self.DocPBCeilingMisc:int = obj["DocPBCeilingMisc"]
      self.DocPBCeilingMtl:int = obj["DocPBCeilingMtl"]
      self.DocPBCeilingMtlBur:int = obj["DocPBCeilingMtlBur"]
      self.DocPBCeilingSub:int = obj["DocPBCeilingSub"]
      self.DocPBCeilingTotal:int = obj["DocPBCeilingTotal"]
      self.DocPBFeeLbrCharge:int = obj["DocPBFeeLbrCharge"]
      self.DocPBFeeMiscCharge:int = obj["DocPBFeeMiscCharge"]
      self.DocPBFeeMtlCharge:int = obj["DocPBFeeMtlCharge"]
      self.DocPBFeeSubCharge:int = obj["DocPBFeeSubCharge"]
      self.DocPPCeilingFees:int = obj["DocPPCeilingFees"]
      self.DocPPCeilingTotal:int = obj["DocPPCeilingTotal"]
      self.DocTotLiqToDate:int = obj["DocTotLiqToDate"]
      self.DocTotPPToDate:int = obj["DocTotPPToDate"]
      self.EndDate:str = obj["EndDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      self.LockRate:bool = obj["LockRate"]
      self.MarkUpID:str = obj["MarkUpID"]
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      self.PBBurMarkUp:int = obj["PBBurMarkUp"]
      self.PBCeilingBur:int = obj["PBCeilingBur"]
      self.PBCeilingFees:int = obj["PBCeilingFees"]
      self.PBCeilingLbr:int = obj["PBCeilingLbr"]
      self.PBCeilingMisc:int = obj["PBCeilingMisc"]
      self.PBCeilingMtl:int = obj["PBCeilingMtl"]
      self.PBCeilingMtlBur:int = obj["PBCeilingMtlBur"]
      self.PBCeilingSub:int = obj["PBCeilingSub"]
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      self.PBDocInvoicedBur:int = obj["PBDocInvoicedBur"]
      self.PBDocInvoicedFees:int = obj["PBDocInvoicedFees"]
      self.PBDocInvoicedLbr:int = obj["PBDocInvoicedLbr"]
      self.PBDocInvoicedMisc:int = obj["PBDocInvoicedMisc"]
      self.PBDocInvoicedMtl:int = obj["PBDocInvoicedMtl"]
      self.PBDocInvoicedMtlBur:int = obj["PBDocInvoicedMtlBur"]
      self.PBDocInvoicedSub:int = obj["PBDocInvoicedSub"]
      self.PBFeeApply:str = obj["PBFeeApply"]
      self.PBFeeApplyOn:str = obj["PBFeeApplyOn"]
      self.PBFeeInvoiceText:str = obj["PBFeeInvoiceText"]
      self.PBFeeLbrApply:str = obj["PBFeeLbrApply"]
      self.PBFeeLbrCharge:int = obj["PBFeeLbrCharge"]
      self.PBFeeLbrType:str = obj["PBFeeLbrType"]
      self.PBFeeMiscApply:str = obj["PBFeeMiscApply"]
      self.PBFeeMiscCharge:int = obj["PBFeeMiscCharge"]
      self.PBFeeMiscType:str = obj["PBFeeMiscType"]
      self.PBFeeMtlApply:str = obj["PBFeeMtlApply"]
      self.PBFeeMtlCharge:int = obj["PBFeeMtlCharge"]
      self.PBFeeMtlType:str = obj["PBFeeMtlType"]
      self.PBFeeProject:int = obj["PBFeeProject"]
      self.PBFeeSubApply:str = obj["PBFeeSubApply"]
      self.PBFeeSubCharge:int = obj["PBFeeSubCharge"]
      self.PBFeeSubType:str = obj["PBFeeSubType"]
      self.PBFeeType:str = obj["PBFeeType"]
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      self.PBLbMarkUp:int = obj["PBLbMarkUp"]
      self.PBMiscMarkUp:int = obj["PBMiscMarkUp"]
      self.PBMtlBurMarkUp:int = obj["PBMtlBurMarkUp"]
      self.PBMtlMarkUp:int = obj["PBMtlMarkUp"]
      self.PBOverridenMU:bool = obj["PBOverridenMU"]
      self.PBPrjRtSrc:str = obj["PBPrjRtSrc"]
      self.PBRetentionPcnt:int = obj["PBRetentionPcnt"]
      self.PBRetentionProc:str = obj["PBRetentionProc"]
      self.PBSubMarkUp:int = obj["PBSubMarkUp"]
      self.PersonList:str = obj["PersonList"]
      self.PPActive:bool = obj["PPActive"]
      self.PPAllowPcnt:int = obj["PPAllowPcnt"]
      self.PPCeilingFees:int = obj["PPCeilingFees"]
      self.PPCeilingTotal:int = obj["PPCeilingTotal"]
      self.PrimaryAsmSeq:int = obj["PrimaryAsmSeq"]
      self.PrimaryJob:str = obj["PrimaryJob"]
      self.PrimaryMtl:int = obj["PrimaryMtl"]
      self.ProdCode:str = obj["ProdCode"]
      self.ProjectID:str = obj["ProjectID"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.RetentionPrcnt:int = obj["RetentionPrcnt"]
      self.RetentionProc:str = obj["RetentionProc"]
      self.Revision:int = obj["Revision"]
      self.Rpt1ConTotInv:int = obj["Rpt1ConTotInv"]
      self.Rpt1ConTotValue:int = obj["Rpt1ConTotValue"]
      self.Rpt1PBCeilingBur:int = obj["Rpt1PBCeilingBur"]
      self.Rpt1PBCeilingFees:int = obj["Rpt1PBCeilingFees"]
      self.Rpt1PBCeilingLbr:int = obj["Rpt1PBCeilingLbr"]
      self.Rpt1PBCeilingMisc:int = obj["Rpt1PBCeilingMisc"]
      self.Rpt1PBCeilingMtl:int = obj["Rpt1PBCeilingMtl"]
      self.Rpt1PBCeilingMtlBur:int = obj["Rpt1PBCeilingMtlBur"]
      self.Rpt1PBCeilingSub:int = obj["Rpt1PBCeilingSub"]
      self.Rpt1PBCeilingTotal:int = obj["Rpt1PBCeilingTotal"]
      self.Rpt1PBFeeLbrCharge:int = obj["Rpt1PBFeeLbrCharge"]
      self.Rpt1PBFeeMiscCharge:int = obj["Rpt1PBFeeMiscCharge"]
      self.Rpt1PBFeeMtlCharge:int = obj["Rpt1PBFeeMtlCharge"]
      self.Rpt1PBFeeSubCharge:int = obj["Rpt1PBFeeSubCharge"]
      self.Rpt1PPCeilingFees:int = obj["Rpt1PPCeilingFees"]
      self.Rpt1PPCeilingTotal:int = obj["Rpt1PPCeilingTotal"]
      self.Rpt1TotLiqToDate:int = obj["Rpt1TotLiqToDate"]
      self.Rpt1TotPPToDate:int = obj["Rpt1TotPPToDate"]
      self.Rpt2ConTotInv:int = obj["Rpt2ConTotInv"]
      self.Rpt2ConTotValue:int = obj["Rpt2ConTotValue"]
      self.Rpt2PBCeilingBur:int = obj["Rpt2PBCeilingBur"]
      self.Rpt2PBCeilingFees:int = obj["Rpt2PBCeilingFees"]
      self.Rpt2PBCeilingLbr:int = obj["Rpt2PBCeilingLbr"]
      self.Rpt2PBCeilingMisc:int = obj["Rpt2PBCeilingMisc"]
      self.Rpt2PBCeilingMtl:int = obj["Rpt2PBCeilingMtl"]
      self.Rpt2PBCeilingMtlBur:int = obj["Rpt2PBCeilingMtlBur"]
      self.Rpt2PBCeilingSub:int = obj["Rpt2PBCeilingSub"]
      self.Rpt2PBCeilingTotal:int = obj["Rpt2PBCeilingTotal"]
      self.Rpt2PBFeeLbrCharge:int = obj["Rpt2PBFeeLbrCharge"]
      self.Rpt2PBFeeMiscCharge:int = obj["Rpt2PBFeeMiscCharge"]
      self.Rpt2PBFeeMtlCharge:int = obj["Rpt2PBFeeMtlCharge"]
      self.Rpt2PBFeeSubCharge:int = obj["Rpt2PBFeeSubCharge"]
      self.Rpt2PPCeilingFees:int = obj["Rpt2PPCeilingFees"]
      self.Rpt2PPCeilingTotal:int = obj["Rpt2PPCeilingTotal"]
      self.Rpt2TotLiqToDate:int = obj["Rpt2TotLiqToDate"]
      self.Rpt2TotPPToDate:int = obj["Rpt2TotPPToDate"]
      self.Rpt3ConTotInv:int = obj["Rpt3ConTotInv"]
      self.Rpt3ConTotValue:int = obj["Rpt3ConTotValue"]
      self.Rpt3PBCeilingBur:int = obj["Rpt3PBCeilingBur"]
      self.Rpt3PBCeilingFees:int = obj["Rpt3PBCeilingFees"]
      self.Rpt3PBCeilingLbr:int = obj["Rpt3PBCeilingLbr"]
      self.Rpt3PBCeilingMisc:int = obj["Rpt3PBCeilingMisc"]
      self.Rpt3PBCeilingMtl:int = obj["Rpt3PBCeilingMtl"]
      self.Rpt3PBCeilingMtlBur:int = obj["Rpt3PBCeilingMtlBur"]
      self.Rpt3PBCeilingSub:int = obj["Rpt3PBCeilingSub"]
      self.Rpt3PBCeilingTotal:int = obj["Rpt3PBCeilingTotal"]
      self.Rpt3PBFeeLbrCharge:int = obj["Rpt3PBFeeLbrCharge"]
      self.Rpt3PBFeeMiscCharge:int = obj["Rpt3PBFeeMiscCharge"]
      self.Rpt3PBFeeMtlCharge:int = obj["Rpt3PBFeeMtlCharge"]
      self.Rpt3PBFeeSubCharge:int = obj["Rpt3PBFeeSubCharge"]
      self.Rpt3PPCeilingFees:int = obj["Rpt3PPCeilingFees"]
      self.Rpt3PPCeilingTotal:int = obj["Rpt3PPCeilingTotal"]
      self.Rpt3TotLiqToDate:int = obj["Rpt3TotLiqToDate"]
      self.Rpt3TotPPToDate:int = obj["Rpt3TotPPToDate"]
      self.SalesCatID:str = obj["SalesCatID"]
      self.StartDate:str = obj["StartDate"]
      self.TotLiqToDate:int = obj["TotLiqToDate"]
      self.TotPPToDate:int = obj["TotPPToDate"]
      self.UserMap:str = obj["UserMap"]
      self.UserMapData:str = obj["UserMapData"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.MtlTaxCatID:str = obj["MtlTaxCatID"]
      self.LbrTaxCatID:str = obj["LbrTaxCatID"]
      self.FeeTaxCatID:str = obj["FeeTaxCatID"]
      self.ODCTaxCatID:str = obj["ODCTaxCatID"]
      self.SubTaxCatID:str = obj["SubTaxCatID"]
      self.BdnTaxCatID:str = obj["BdnTaxCatID"]
      self.RetTaxCatID:str = obj["RetTaxCatID"]
      self.TaxOnNetOfRet:bool = obj["TaxOnNetOfRet"]
      self.CeilTaxCatID:str = obj["CeilTaxCatID"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LastAction:str = obj["LastAction"]
      """  LastAction  """  
      self.ActionDate:str = obj["ActionDate"]
      """  ActionDate  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HXProjectSearchTableset:
   def __init__(self, obj):
      self.HXProject:list[Erp_Tablesets_HXProjectRow] = obj["HXProject"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtHXProjectSearchTableset:
   def __init__(self, obj):
      self.HXProject:list[Erp_Tablesets_HXProjectRow] = obj["HXProject"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   projectID
   revision
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      self.revision:int = obj["revision"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HXProjectSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_HXProjectSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_HXProjectSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_HXProjectListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewHXProject_input:
   """ Required : 
   ds
   projectID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HXProjectSearchTableset] = obj["ds"]
      self.projectID:str = obj["projectID"]
      pass

class GetNewHXProject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HXProjectSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseHXProject
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseHXProject:str = obj["whereClauseHXProject"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HXProjectSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtHXProjectSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtHXProjectSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HXProjectSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HXProjectSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

