import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.PublishedViewSvc
# Description: The Published View service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PublishedViews(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PublishedViews items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PublishedViews
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PublishedViewRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/PublishedViews",headers=creds) as resp:
           return await resp.json()

async def post_PublishedViews(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PublishedViews
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.PublishedViewRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.PublishedViewRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/PublishedViews", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PublishedViews_Company_DynamicQueryID_ProductID_DefinitionID_Approved_UserID_GlbCompany_ViewID(Company, DynamicQueryID, ProductID, DefinitionID, Approved, UserID, GlbCompany, ViewID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PublishedView item
   Description: Calls GetByID to retrieve the PublishedView item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PublishedView
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DynamicQueryID: Desc: DynamicQueryID   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param Approved: Desc: Approved   Required: True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param ViewID: Desc: ViewID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PublishedViewRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/PublishedViews(" + Company + "," + DynamicQueryID + "," + ProductID + "," + DefinitionID + "," + Approved + "," + UserID + "," + GlbCompany + "," + ViewID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PublishedViews_Company_DynamicQueryID_ProductID_DefinitionID_Approved_UserID_GlbCompany_ViewID(Company, DynamicQueryID, ProductID, DefinitionID, Approved, UserID, GlbCompany, ViewID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PublishedView for the service
   Description: Calls UpdateExt to update PublishedView. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PublishedView
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DynamicQueryID: Desc: DynamicQueryID   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param Approved: Desc: Approved   Required: True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param ViewID: Desc: ViewID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.PublishedViewRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/PublishedViews(" + Company + "," + DynamicQueryID + "," + ProductID + "," + DefinitionID + "," + Approved + "," + UserID + "," + GlbCompany + "," + ViewID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PublishedViews_Company_DynamicQueryID_ProductID_DefinitionID_Approved_UserID_GlbCompany_ViewID(Company, DynamicQueryID, ProductID, DefinitionID, Approved, UserID, GlbCompany, ViewID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PublishedView item
   Description: Call UpdateExt to delete PublishedView item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PublishedView
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DynamicQueryID: Desc: DynamicQueryID   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param Approved: Desc: Approved   Required: True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param ViewID: Desc: ViewID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/PublishedViews(" + Company + "," + DynamicQueryID + "," + ProductID + "," + DefinitionID + "," + Approved + "," + UserID + "," + GlbCompany + "," + ViewID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PublishedViewListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePublishedView, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePublishedView=" + whereClausePublishedView
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(dynamicQueryID, productID, definitionID, approved, userID, glbCompany, viewID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
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
   params += "dynamicQueryID=" + dynamicQueryID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "productID=" + productID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "definitionID=" + definitionID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "approved=" + approved
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "userID=" + userID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glbCompany=" + glbCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "viewID=" + viewID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPublishedView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPublishedView
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPublishedView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPublishedView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPublishedView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PublishedViewSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PublishedViewListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PublishedViewListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PublishedViewRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PublishedViewRow] = obj["value"]
      pass

class Ice_Tablesets_PublishedViewListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DynamicQueryID:str = obj["DynamicQueryID"]
      """  Dynamic Query ID  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Definition ID  """  
      self.Approved:bool = obj["Approved"]
      """   no = this exports is a work-in-process one
Since 9.0 there should be only approved BAQs.  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.ViewID:str = obj["ViewID"]
      """  View ID  """  
      self.Caption:str = obj["Caption"]
      """  Caption  """  
      self.InstallView:bool = obj["InstallView"]
      """  Install View  """  
      self.ImageName:str = obj["ImageName"]
      """  Image Name  """  
      self.System:bool = obj["System"]
      """  Flag to indicate Published view is created by Epicor  """  
      self.IsShared:bool = obj["IsShared"]
      """  Flag to indicate Published view is shared  """  
      self.PublishedBy:str = obj["PublishedBy"]
      """  Who published the dashboard view  """  
      self.ViewType:str = obj["ViewType"]
      """  Type of dashboard View  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.PVGroup:str = obj["PVGroup"]
      """  PVGroup  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DashBdDefDescription:str = obj["DashBdDefDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PublishedViewRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DynamicQueryID:str = obj["DynamicQueryID"]
      """  Dynamic Query ID  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Definition ID  """  
      self.Approved:bool = obj["Approved"]
      """   no = this exports is a work-in-process one
Since 9.0 there should be only approved BAQs.  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.ViewID:str = obj["ViewID"]
      """  View ID  """  
      self.Caption:str = obj["Caption"]
      """  Caption  """  
      self.InstallView:bool = obj["InstallView"]
      """  Install View  """  
      self.ImageName:str = obj["ImageName"]
      """  Image Name  """  
      self.System:bool = obj["System"]
      """  Flag to indicate Published view is created by Epicor  """  
      self.IsShared:bool = obj["IsShared"]
      """  Flag to indicate Published view is shared  """  
      self.PublishedBy:str = obj["PublishedBy"]
      """  Who published the dashboard view  """  
      self.ViewType:str = obj["ViewType"]
      """  Type of dashboard View  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.PVGroup:str = obj["PVGroup"]
      """  PVGroup  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DashBdDefDescription:str = obj["DashBdDefDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   dynamicQueryID
   productID
   definitionID
   approved
   userID
   glbCompany
   viewID
   """  
   def __init__(self, obj):
      self.dynamicQueryID:str = obj["dynamicQueryID"]
      self.productID:str = obj["productID"]
      self.definitionID:str = obj["definitionID"]
      self.approved:bool = obj["approved"]
      self.userID:str = obj["userID"]
      self.glbCompany:str = obj["glbCompany"]
      self.viewID:str = obj["viewID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   dynamicQueryID
   productID
   definitionID
   approved
   userID
   glbCompany
   viewID
   """  
   def __init__(self, obj):
      self.dynamicQueryID:str = obj["dynamicQueryID"]
      self.productID:str = obj["productID"]
      self.definitionID:str = obj["definitionID"]
      self.approved:bool = obj["approved"]
      self.userID:str = obj["userID"]
      self.glbCompany:str = obj["glbCompany"]
      self.viewID:str = obj["viewID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PublishedViewTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_PublishedViewTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_PublishedViewTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_PublishedViewListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPublishedView_input:
   """ Required : 
   ds
   dynamicQueryID
   productID
   definitionID
   approved
   userID
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_PublishedViewTableset] = obj["ds"]
      self.dynamicQueryID:str = obj["dynamicQueryID"]
      self.productID:str = obj["productID"]
      self.definitionID:str = obj["definitionID"]
      self.approved:bool = obj["approved"]
      self.userID:str = obj["userID"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewPublishedView_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_PublishedViewTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePublishedView
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePublishedView:str = obj["whereClausePublishedView"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PublishedViewTableset] = obj["returnObj"]
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

class Ice_Tablesets_PublishedViewListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DynamicQueryID:str = obj["DynamicQueryID"]
      """  Dynamic Query ID  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Definition ID  """  
      self.Approved:bool = obj["Approved"]
      """   no = this exports is a work-in-process one
Since 9.0 there should be only approved BAQs.  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.ViewID:str = obj["ViewID"]
      """  View ID  """  
      self.Caption:str = obj["Caption"]
      """  Caption  """  
      self.InstallView:bool = obj["InstallView"]
      """  Install View  """  
      self.ImageName:str = obj["ImageName"]
      """  Image Name  """  
      self.System:bool = obj["System"]
      """  Flag to indicate Published view is created by Epicor  """  
      self.IsShared:bool = obj["IsShared"]
      """  Flag to indicate Published view is shared  """  
      self.PublishedBy:str = obj["PublishedBy"]
      """  Who published the dashboard view  """  
      self.ViewType:str = obj["ViewType"]
      """  Type of dashboard View  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.PVGroup:str = obj["PVGroup"]
      """  PVGroup  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DashBdDefDescription:str = obj["DashBdDefDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PublishedViewListTableset:
   def __init__(self, obj):
      self.PublishedViewList:list[Ice_Tablesets_PublishedViewListRow] = obj["PublishedViewList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_PublishedViewRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DynamicQueryID:str = obj["DynamicQueryID"]
      """  Dynamic Query ID  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Definition ID  """  
      self.Approved:bool = obj["Approved"]
      """   no = this exports is a work-in-process one
Since 9.0 there should be only approved BAQs.  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.ViewID:str = obj["ViewID"]
      """  View ID  """  
      self.Caption:str = obj["Caption"]
      """  Caption  """  
      self.InstallView:bool = obj["InstallView"]
      """  Install View  """  
      self.ImageName:str = obj["ImageName"]
      """  Image Name  """  
      self.System:bool = obj["System"]
      """  Flag to indicate Published view is created by Epicor  """  
      self.IsShared:bool = obj["IsShared"]
      """  Flag to indicate Published view is shared  """  
      self.PublishedBy:str = obj["PublishedBy"]
      """  Who published the dashboard view  """  
      self.ViewType:str = obj["ViewType"]
      """  Type of dashboard View  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.PVGroup:str = obj["PVGroup"]
      """  PVGroup  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DashBdDefDescription:str = obj["DashBdDefDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PublishedViewTableset:
   def __init__(self, obj):
      self.PublishedView:list[Ice_Tablesets_PublishedViewRow] = obj["PublishedView"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtPublishedViewTableset:
   def __init__(self, obj):
      self.PublishedView:list[Ice_Tablesets_PublishedViewRow] = obj["PublishedView"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtPublishedViewTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtPublishedViewTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_PublishedViewTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_PublishedViewTableset] = obj["ds"]
      pass

      """  output parameters  """  

