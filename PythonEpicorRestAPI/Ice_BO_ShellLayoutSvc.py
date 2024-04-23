import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ShellLayoutSvc
# Description: Service for managing IceShell layouts
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ShellLayouts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShellLayouts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShellLayouts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ShellLayoutRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts",headers=creds) as resp:
           return await resp.json()

async def post_ShellLayouts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShellLayouts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ShellLayoutRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ShellLayoutRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShellLayouts_TenantID_HomePageType_SubType_LayoutID(TenantID, HomePageType, SubType, LayoutID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShellLayout item
   Description: Calls GetByID to retrieve the ShellLayout item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShellLayout
      :param TenantID: Desc: TenantID   Required: True   Allow empty value : True
      :param HomePageType: Desc: HomePageType   Required: True   Allow empty value : True
      :param SubType: Desc: SubType   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ShellLayoutRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts(" + TenantID + "," + HomePageType + "," + SubType + "," + LayoutID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShellLayouts_TenantID_HomePageType_SubType_LayoutID(TenantID, HomePageType, SubType, LayoutID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShellLayout for the service
   Description: Calls UpdateExt to update ShellLayout. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShellLayout
      :param TenantID: Desc: TenantID   Required: True   Allow empty value : True
      :param HomePageType: Desc: HomePageType   Required: True   Allow empty value : True
      :param SubType: Desc: SubType   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ShellLayoutRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts(" + TenantID + "," + HomePageType + "," + SubType + "," + LayoutID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShellLayouts_TenantID_HomePageType_SubType_LayoutID(TenantID, HomePageType, SubType, LayoutID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShellLayout item
   Description: Call UpdateExt to delete ShellLayout item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShellLayout
      :param TenantID: Desc: TenantID   Required: True   Allow empty value : True
      :param HomePageType: Desc: HomePageType   Required: True   Allow empty value : True
      :param SubType: Desc: SubType   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/ShellLayouts(" + TenantID + "," + HomePageType + "," + SubType + "," + LayoutID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ShellLayoutListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseShellLayout, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseShellLayout=" + whereClauseShellLayout
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tenantID, homePageType, subType, layoutID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "tenantID=" + tenantID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "homePageType=" + homePageType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "subType=" + subType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "layoutID=" + layoutID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultLayout
   Description: Get Layout for user
   OperationID: GetDefaultLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetToDefaultLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetToDefaultLayout
   Description: Resets to default layout.
   OperationID: ResetToDefaultLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetToDefaultLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetToDefaultLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetAsSystemDefaultLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetAsSystemDefaultLayout
   Description: Sets the specified published layout as the system default layout for the homepage type.
   OperationID: SetAsSystemDefaultLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAsSystemDefaultLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAsSystemDefaultLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsLayoutPublished(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsLayoutPublished
   Description: Checks if layout is published.
   OperationID: IsLayoutPublished
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsLayoutPublished_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsLayoutPublished_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPublishedShellLayouts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPublishedShellLayouts
   Description: Gets the published layouts.
   OperationID: GetPublishedShellLayouts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPublishedShellLayouts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPublishedShellLayouts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIfUserHasAccessToLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIfUserHasAccessToLayout
   Description: Checks if user has access to layout.
   OperationID: CheckIfUserHasAccessToLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfUserHasAccessToLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfUserHasAccessToLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSecurityCodeForPublishedLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSecurityCodeForPublishedLayout
   Description: Updates the security code for published layout.
   OperationID: UpdateSecurityCodeForPublishedLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSecurityCodeForPublishedLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSecurityCodeForPublishedLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PublishLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PublishLayout
   Description: Publishes the layout from the ShellLayoutPersonal into the ShellLayout table.
   OperationID: PublishLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnpublishLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnpublishLayout
   Description: Unpublishes the layout if it is un-used.
   OperationID: UnpublishLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnpublishLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnpublishLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectPublishedLayoutForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectPublishedLayoutForUser
   Description: Selects the published layout for user.
   OperationID: SelectPublishedLayoutForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectPublishedLayoutForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectPublishedLayoutForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveShellLayoutAsPersonal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveShellLayoutAsPersonal
   Description: Saves the published layout as personal.
   OperationID: SaveShellLayoutAsPersonal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveShellLayoutAsPersonal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveShellLayoutAsPersonal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsCurrentPersonalLayoutReadonly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsCurrentPersonalLayoutReadonly
   Description: Determines whether the user's layout is non-editable (published or system layout).
   OperationID: IsCurrentPersonalLayoutReadonly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsCurrentPersonalLayoutReadonly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsCurrentPersonalLayoutReadonly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentCompanySiteLogo(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentCompanySiteLogo
   Description: Gets the current company site logo.
   OperationID: GetCurrentCompanySiteLogo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentCompanySiteLogo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ExportShellLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportShellLayout
   Description: Exports the shell layout.
   OperationID: ExportShellLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportShellLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportShellLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportShellLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportShellLayout
   Description: Imports the shell layout.
   OperationID: ImportShellLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportShellLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportShellLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPersonalShellLayoutForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPersonalShellLayoutForUser
   Description: Gets the personal shell layout for user.
   OperationID: GetPersonalShellLayoutForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPersonalShellLayoutForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPersonalShellLayoutForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHomePageForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHomePageForUser
   Description: Gets the home page for user.
   OperationID: GetHomePageForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHomePageForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHomePageForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateHomePageForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateHomePageForUser
   Description: Updates the home page for user.
   OperationID: UpdateHomePageForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateHomePageForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateHomePageForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUserOptionsForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUserOptionsForUser
   Description: Gets the user options for user.
   OperationID: GetUserOptionsForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUserOptionsForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserOptionsForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateUserOptionsForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateUserOptionsForUser
   Description: Updates the user options for user.
   OperationID: UpdateUserOptionsForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateUserOptionsForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateUserOptionsForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetImageForTile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetImageForTile
   Description: Gets the image for tile.
   OperationID: GetImageForTile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetImageForTile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetImageForTile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveImageForTile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveImageForTile
   Description: Saves the image for tile.
   OperationID: SaveImageForTile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveImageForTile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveImageForTile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataDiscoveryUrl(epicorHeaders = None):
   """  
   Summary: Invoke method GetDataDiscoveryUrl
   Description: Gets the data discovery URL from the system configuration.
   OperationID: GetDataDiscoveryUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataDiscoveryUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SaveDataDiscoveryUrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveDataDiscoveryUrl
   Description: Saves the data discovery URL to the system configuration.
   OperationID: SaveDataDiscoveryUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveDataDiscoveryUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDataDiscoveryUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShellLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShellLayout
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShellLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShellLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShellLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ShellLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ShellLayoutListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ShellLayoutListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ShellLayoutRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ShellLayoutRow] = obj["value"]
      pass

class Ice_Tablesets_ShellLayoutListRow:
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID  """  
      self.AuthorID:str = obj["AuthorID"]
      """  AuthorID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SecCode:str = obj["SecCode"]
      """  SecCode  """  
      self.Published:bool = obj["Published"]
      """  Published  """  
      self.HomePageType:str = obj["HomePageType"]
      """  HomePageType  """  
      self.SubType:str = obj["SubType"]
      """  SubType  """  
      self.LayoutDescription:str = obj["LayoutDescription"]
      """  LayoutDescription  """  
      self.IsHomeDefault:bool = obj["IsHomeDefault"]
      """  IsHomeDefault  """  
      self.Version:str = obj["Version"]
      """  Version of the release this layout was exported from.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ShellLayoutRow:
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID  """  
      self.AuthorID:str = obj["AuthorID"]
      """  AuthorID  """  
      self.DateModified:str = obj["DateModified"]
      """  DateModified  """  
      self.ShellHomePage:str = obj["ShellHomePage"]
      """  ShellHomePage  """  
      self.ShellUserOptions:str = obj["ShellUserOptions"]
      """  ShellUserOptions  """  
      self.FavoriteItems:str = obj["FavoriteItems"]
      """  FavoriteItems  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SecCode:str = obj["SecCode"]
      """  SecCode  """  
      self.Published:bool = obj["Published"]
      """  Published  """  
      self.HomePageType:str = obj["HomePageType"]
      """  HomePageType  """  
      self.SubType:str = obj["SubType"]
      """  SubType  """  
      self.LayoutDescription:str = obj["LayoutDescription"]
      """  LayoutDescription  """  
      self.IsHomeDefault:bool = obj["IsHomeDefault"]
      """  IsHomeDefault  """  
      self.Version:str = obj["Version"]
      """  Version of the release this layout was exported from.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckIfUserHasAccessToLayout_input:
   """ Required : 
   layoutId
   userId
   homePageType
   subType
   """  
   def __init__(self, obj):
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier.  """  
      self.userId:str = obj["userId"]
      """  The user identifier.  """  
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      pass

class CheckIfUserHasAccessToLayout_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   tenantID
   homePageType
   subType
   layoutID
   """  
   def __init__(self, obj):
      self.tenantID:str = obj["tenantID"]
      self.homePageType:str = obj["homePageType"]
      self.subType:str = obj["subType"]
      self.layoutID:str = obj["layoutID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class ExportShellLayout_input:
   """ Required : 
   homePageType
   subType
   layoutId
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier.  """  
      pass

class ExportShellLayout_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Serialized ShellLayoutDataSet.  """  
      pass

class GetByID_input:
   """ Required : 
   tenantID
   homePageType
   subType
   layoutID
   """  
   def __init__(self, obj):
      self.tenantID:str = obj["tenantID"]
      self.homePageType:str = obj["homePageType"]
      self.subType:str = obj["subType"]
      self.layoutID:str = obj["layoutID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ShellLayoutTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ShellLayoutTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ShellLayoutTableset] = obj["returnObj"]
      pass

class GetCurrentCompanySiteLogo_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Default logo for current Company or Site, if defined.  """  
      pass

class GetDataDiscoveryUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDefaultLayout_input:
   """ Required : 
   homePageType
   subType
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page (ERP, CRM, MES).  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      pass

class GetDefaultLayout_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ShellLayoutTableset] = obj["returnObj"]
      pass

class GetHomePageForUser_input:
   """ Required : 
   homePageType
   subType
   layoutId
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier.  """  
      pass

class GetHomePageForUser_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_HomePageTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.warningLayoutNoAccess:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetImageForTile_input:
   """ Required : 
   imageId
   """  
   def __init__(self, obj):
      self.imageId:str = obj["imageId"]
      """  The image identifier.  """  
      pass

class GetImageForTile_output:
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
      self.returnObj:list[Ice_Tablesets_ShellLayoutListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewShellLayout_input:
   """ Required : 
   ds
   tenantID
   homePageType
   subType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ShellLayoutTableset] = obj["ds"]
      self.tenantID:str = obj["tenantID"]
      self.homePageType:str = obj["homePageType"]
      self.subType:str = obj["subType"]
      pass

class GetNewShellLayout_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ShellLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPersonalShellLayoutForUser_input:
   """ Required : 
   homePageType
   subType
   layoutId
   homePageData
   userOptionsData
   favoritesData
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier.  """  
      self.homePageData:list[Ice_Tablesets_HomePageTableset] = obj["homePageData"]
      self.userOptionsData:list[Ice_Tablesets_UserOptionsTableset] = obj["userOptionsData"]
      self.favoritesData:list[Ice_Tablesets_FavoriteTableset] = obj["favoritesData"]
      pass

class GetPersonalShellLayoutForUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.homePageData:list[Ice_Tablesets_HomePageTableset] = obj["homePageData"]
      self.userOptionsData:list[Ice_Tablesets_UserOptionsTableset] = obj["userOptionsData"]
      self.favoritesData:list[Ice_Tablesets_FavoriteTableset] = obj["favoritesData"]
      self.warningNoAccess:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPublishedShellLayouts_input:
   """ Required : 
   homePageType
   subType
   includeSystemLayouts
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.includeSystemLayouts:bool = obj["includeSystemLayouts"]
      """  if set to `true` [include system layouts].  """  
      pass

class GetPublishedShellLayouts_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ShellLayoutListTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseShellLayout
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShellLayout:str = obj["whereClauseShellLayout"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ShellLayoutTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetUserOptionsForUser_input:
   """ Required : 
   homePageType
   subType
   layoutId
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier. Pass empty string for 'modern' subtype.  """  
      pass

class GetUserOptionsForUser_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UserOptionsTableset] = obj["returnObj"]
      pass

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

class Ice_Tablesets_FavFolderRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      self.FolderSeq:int = obj["FolderSeq"]
      self.Description:str = obj["Description"]
      self.YPos:int = obj["YPos"]
      self.AutoLoadContents:bool = obj["AutoLoadContents"]
      self.AutoLoadSessionChange:bool = obj["AutoLoadSessionChange"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_FavItemsRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      self.FolderSeq:int = obj["FolderSeq"]
      self.ItemSeq:int = obj["ItemSeq"]
      self.ItemType:str = obj["ItemType"]
      self.ItemName:str = obj["ItemName"]
      self.Description:str = obj["Description"]
      self.MenuName:str = obj["MenuName"]
      self.YPos:int = obj["YPos"]
      self.AppServerURL:str = obj["AppServerURL"]
      self.CompanyID:str = obj["CompanyID"]
      self.PlantID:str = obj["PlantID"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.FolderSeqDescription:str = obj["FolderSeqDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_FavoriteTableset:
   def __init__(self, obj):
      self.FavFolder:list[Ice_Tablesets_FavFolderRow] = obj["FavFolder"]
      self.FavItems:list[Ice_Tablesets_FavItemsRow] = obj["FavItems"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_HomePageTableset:
   def __init__(self, obj):
      self.HomeTileGroup:list[Ice_Tablesets_HomeTileGroupRow] = obj["HomeTileGroup"]
      self.HomeTile:list[Ice_Tablesets_HomeTileRow] = obj["HomeTile"]
      self.LayoutInfo:list[Ice_Tablesets_LayoutInfoRow] = obj["LayoutInfo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_HomeTileGroupRow:
   def __init__(self, obj):
      self.GroupID:int = obj["GroupID"]
      self.Title:str = obj["Title"]
      """  Title of the group of tiles.  """  
      self.IsFaveDefault:bool = obj["IsFaveDefault"]
      """  If this is the default Favorites group.  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence of this group on the home page.  """  
      self.WebProperties:str = obj["WebProperties"]
      """  Stores tile settings as required by the web home page in a Json format.  """  
      self.Type:str = obj["Type"]
      """  The type of group.  """  
      self.Retain:bool = obj["Retain"]
      """  Marks the tile group to be retained when no longer the active tab.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_HomeTileRow:
   def __init__(self, obj):
      self.TileID:int = obj["TileID"]
      """  Tile identifier  """  
      self.GroupID:int = obj["GroupID"]
      """  Group that this tile belongs to.  """  
      self.Type:str = obj["Type"]
      """   Type of tile:                 
Baq = "B";
Favorite = "V";
General = "G";
Link = "K";
Social = "S";
DataDiscovery = "Y";
Metric = "M";

to be removed "soon".
List = "L";
Custom = "T";

UnknownA = "A";
UnknownD = "D";
UnknownF = "F";
UnknownU = "U";  """  
      self.Path:str = obj["Path"]
      """  URL or file paths for the tile.  """  
      self.LinkType:str = obj["LinkType"]
      """   Type of link on tile.         
File = "P";
Form = "F";
NoAction = "N";
Url = "U";  """  
      self.DisplayType:str = obj["DisplayType"]
      """   Display type for tile:        
Default = "D";
Image = "I";
Url = "U";  """  
      self.DisplayPath:str = obj["DisplayPath"]
      self.LineLinkType:str = obj["LineLinkType"]
      """   Possible values:              
File = "P";
Form = "F";
NoAction = "N";
Url = "U";  """  
      self.LinePath:str = obj["LinePath"]
      """  URL/path for the BAQ tiles.  """  
      self.BaqId:str = obj["BaqId"]
      """  BAQ identifier if tile displays a BAQ.  """  
      self.Color:str = obj["Color"]
      """  Color  """  
      self.Title:str = obj["Title"]
      """  Tile title  """  
      self.DefaultWidth:int = obj["DefaultWidth"]
      """  Default width of the tile  """  
      self.DefaultHeight:int = obj["DefaultHeight"]
      """  Default height of the tile.  """  
      self.MaxWidth:int = obj["MaxWidth"]
      """  Maximum width of the tile.  """  
      self.MaxHeight:int = obj["MaxHeight"]
      """  Maximum height of the tile.  """  
      self.ListImage:str = obj["ListImage"]
      """  Identifier to the image displayed for the baq.  """  
      self.FavoriteFolderSeq:int = obj["FavoriteFolderSeq"]
      """  Folder sequence for the favorite folder this tile represents.  """  
      self.ExpandedFlag:bool = obj["ExpandedFlag"]
      """  If tile is in expanded state.  """  
      self.BaqColumnList:str = obj["BaqColumnList"]
      """  List of Baq columns to display.  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence of the tile.  """  
      self.RelatedMenuId:str = obj["RelatedMenuId"]
      """  Menu id that the tile represents.  """  
      self.RefreshInterval:int = obj["RefreshInterval"]
      """  Interval between refresh of tile data.  """  
      self.Company:str = obj["Company"]
      """  Company if the user made the tile company-specific.  """  
      self.Appserver:str = obj["Appserver"]
      """  Appserver Url if tile is company specific.  """  
      self.BaqContextColumn:str = obj["BaqContextColumn"]
      """  BaqContextColumn  """  
      self.Plant:str = obj["Plant"]
      """  Site if tile is company/site specific.  """  
      self.MetricAggregate:str = obj["MetricAggregate"]
      """   Aggregation function to perform on the BAQ results. 
SUM, AVG,COUNT,COUNT_STAR,MIN,MAX  """  
      self.MetricTextPrefix:str = obj["MetricTextPrefix"]
      """  Prefix for Metric tile.  """  
      self.MetricTextSuffix:str = obj["MetricTextSuffix"]
      """  Suffix for text displayed in Metric tile.  """  
      self.MetricImage:str = obj["MetricImage"]
      """  Image identifier for the metric tile.  """  
      self.MetricTextFontSize:int = obj["MetricTextFontSize"]
      """  Font size for Metric tile.  """  
      self.ImageRowID:str = obj["ImageRowID"]
      """  SysRowID into FileStore for the image used by the tile.  """  
      self.ImageBlob:str = obj["ImageBlob"]
      """  Contains the image contents of the ImageRowID image.  """  
      self.ImageFilename:str = obj["ImageFilename"]
      """  FileName from Ice.FileStore - only used during import and export.  """  
      self.WebProperties:str = obj["WebProperties"]
      """  Stores tile settings as required by the web home page in a Json format.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LayoutInfoRow:
   def __init__(self, obj):
      self.BaseLayoutID:str = obj["BaseLayoutID"]
      """  Published layout that this layout is connected to.  """  
      self.IsDefaultLayout:bool = obj["IsDefaultLayout"]
      """  Indicates if this is a system default layout.  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID from Ice.ShellLayoutPersonal  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ShellLayoutListRow:
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID  """  
      self.AuthorID:str = obj["AuthorID"]
      """  AuthorID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SecCode:str = obj["SecCode"]
      """  SecCode  """  
      self.Published:bool = obj["Published"]
      """  Published  """  
      self.HomePageType:str = obj["HomePageType"]
      """  HomePageType  """  
      self.SubType:str = obj["SubType"]
      """  SubType  """  
      self.LayoutDescription:str = obj["LayoutDescription"]
      """  LayoutDescription  """  
      self.IsHomeDefault:bool = obj["IsHomeDefault"]
      """  IsHomeDefault  """  
      self.Version:str = obj["Version"]
      """  Version of the release this layout was exported from.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ShellLayoutListTableset:
   def __init__(self, obj):
      self.ShellLayoutList:list[Ice_Tablesets_ShellLayoutListRow] = obj["ShellLayoutList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ShellLayoutRow:
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID  """  
      self.AuthorID:str = obj["AuthorID"]
      """  AuthorID  """  
      self.DateModified:str = obj["DateModified"]
      """  DateModified  """  
      self.ShellHomePage:str = obj["ShellHomePage"]
      """  ShellHomePage  """  
      self.ShellUserOptions:str = obj["ShellUserOptions"]
      """  ShellUserOptions  """  
      self.FavoriteItems:str = obj["FavoriteItems"]
      """  FavoriteItems  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SecCode:str = obj["SecCode"]
      """  SecCode  """  
      self.Published:bool = obj["Published"]
      """  Published  """  
      self.HomePageType:str = obj["HomePageType"]
      """  HomePageType  """  
      self.SubType:str = obj["SubType"]
      """  SubType  """  
      self.LayoutDescription:str = obj["LayoutDescription"]
      """  LayoutDescription  """  
      self.IsHomeDefault:bool = obj["IsHomeDefault"]
      """  IsHomeDefault  """  
      self.Version:str = obj["Version"]
      """  Version of the release this layout was exported from.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ShellLayoutTableset:
   def __init__(self, obj):
      self.ShellLayout:list[Ice_Tablesets_ShellLayoutRow] = obj["ShellLayout"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtShellLayoutTableset:
   def __init__(self, obj):
      self.ShellLayout:list[Ice_Tablesets_ShellLayoutRow] = obj["ShellLayout"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UserOptionsRow:
   def __init__(self, obj):
      self.HomePageTileDepth:int = obj["HomePageTileDepth"]
      """  Tile depth for home page.  """  
      self.LastMenuFolderOpened:str = obj["LastMenuFolderOpened"]
      """  Menu that the user was on in the last session.  """  
      self.LastViewDisplayed:str = obj["LastViewDisplayed"]
      """  Last menu view (zoom or tree) that user had.  """  
      self.ContentsView:str = obj["ContentsView"]
      """  View within the contents panel for the menu (icons or list)  """  
      self.Palette:str = obj["Palette"]
      """  Palette picked by the user.  """  
      self.EddTheme:str = obj["EddTheme"]
      """  Edd theme picked by the user - Light/Dark.  """  
      self.Color1:str = obj["Color1"]
      """  Color  """  
      self.Color2:str = obj["Color2"]
      """  Color  """  
      self.Color3:str = obj["Color3"]
      """  Color  """  
      self.Color4:str = obj["Color4"]
      """  Color  """  
      self.Color5:str = obj["Color5"]
      """  Color  """  
      self.Background1:str = obj["Background1"]
      """  Background color selection  """  
      self.Background2:str = obj["Background2"]
      """  Background color selection  """  
      self.Background3:str = obj["Background3"]
      """  Background color selection  """  
      self.Background4:str = obj["Background4"]
      """  Background color selection  """  
      self.ColorBars:str = obj["ColorBars"]
      self.ShowSplashText:bool = obj["ShowSplashText"]
      self.ShowSplashAnimation:bool = obj["ShowSplashAnimation"]
      self.SplashText1:str = obj["SplashText1"]
      self.SplashText2:str = obj["SplashText2"]
      self.SplashText3:str = obj["SplashText3"]
      self.SplashText4:str = obj["SplashText4"]
      self.SplashText5:str = obj["SplashText5"]
      self.SplashText6:str = obj["SplashText6"]
      self.MenuTreeZoomLevel:int = obj["MenuTreeZoomLevel"]
      self.SearchProviders:str = obj["SearchProviders"]
      self.LaunchClassicMenu:bool = obj["LaunchClassicMenu"]
      """  Launch classic menu after log in.  """  
      self.ShowLoadingFormAnnimation:bool = obj["ShowLoadingFormAnnimation"]
      """  Show animation when form is being launched.  """  
      self.HomePageSize:str = obj["HomePageSize"]
      """  Last size of the home page.  """  
      self.HomePageLocation:str = obj["HomePageLocation"]
      """  HomePageLocation  """  
      self.MainFontColor:str = obj["MainFontColor"]
      """  MainFontColor  """  
      self.ShowMenuAnimation:bool = obj["ShowMenuAnimation"]
      self.AppLogoFile:str = obj["AppLogoFile"]
      """  File path to the logo displayed on home page.  """  
      self.DefaultFontFamily:str = obj["DefaultFontFamily"]
      self.DefaultFontWeight:str = obj["DefaultFontWeight"]
      self.DefaultFontSize:int = obj["DefaultFontSize"]
      self.CompanyID:str = obj["CompanyID"]
      """  Company  """  
      self.ColorsStorage:str = obj["ColorsStorage"]
      """  Colors picked by the user stored as a json.  """  
      self.AppLogoRowID:str = obj["AppLogoRowID"]
      """  SysRowID for the image row in Ice.FileStore.  """  
      self.AppLogoBlob:str = obj["AppLogoBlob"]
      """  Contains the image contents of theAppLogoRowID image.  """  
      self.AppLogoFilename:str = obj["AppLogoFilename"]
      """  FileName from Ice.FileStore. Only used during Import/Export.  """  
      self.WebProperties:str = obj["WebProperties"]
      """  Stores tile settings as required by the web home page in a Json format.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UserOptionsTableset:
   def __init__(self, obj):
      self.UserOptions:list[Ice_Tablesets_UserOptionsRow] = obj["UserOptions"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportShellLayout_input:
   """ Required : 
   layoutToImport
   homePageType
   subType
   layoutId
   replaceFavorites
   importedHomepageData
   importedUseroptionsData
   importedFavoritesData
   """  
   def __init__(self, obj):
      self.layoutToImport:str = obj["layoutToImport"]
      """  The layout to import.  """  
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier into which the new layout should be imported.  """  
      self.replaceFavorites:bool = obj["replaceFavorites"]
      """  if set to `true` replaces the current user's favorites with the ones from the imported layout.  """  
      self.importedHomepageData:list[Ice_Tablesets_HomePageTableset] = obj["importedHomepageData"]
      self.importedUseroptionsData:list[Ice_Tablesets_UserOptionsTableset] = obj["importedUseroptionsData"]
      self.importedFavoritesData:list[Ice_Tablesets_FavoriteTableset] = obj["importedFavoritesData"]
      pass

class ImportShellLayout_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.importedHomepageData:list[Ice_Tablesets_HomePageTableset] = obj["importedHomepageData"]
      self.importedUseroptionsData:list[Ice_Tablesets_UserOptionsTableset] = obj["importedUseroptionsData"]
      self.importedFavoritesData:list[Ice_Tablesets_FavoriteTableset] = obj["importedFavoritesData"]
      pass

      """  output parameters  """  

class IsCurrentPersonalLayoutReadonly_input:
   """ Required : 
   homePageType
   subType
   layoutId
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier.  """  
      pass

class IsCurrentPersonalLayoutReadonly_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if user's layout is a published or system layout, otherwise, `false`.  """  
      pass

class IsLayoutPublished_input:
   """ Required : 
   layoutId
   homePageType
   subType
   """  
   def __init__(self, obj):
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier.  """  
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      pass

class IsLayoutPublished_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if layout is published; otherwise, `false`.  """  
      pass

class PublishLayout_input:
   """ Required : 
   personalLayoutId
   publishedLayoutId
   securityCode
   homePageType
   subType
   """  
   def __init__(self, obj):
      self.personalLayoutId:str = obj["personalLayoutId"]
      """  The personal layout identifier to publish.  """  
      self.publishedLayoutId:str = obj["publishedLayoutId"]
      """  The layout identifier for the published layout.  """  
      self.securityCode:str = obj["securityCode"]
      """  The security code.  """  
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      pass

class PublishLayout_output:
   def __init__(self, obj):
      pass

class ResetToDefaultLayout_input:
   """ Required : 
   homePageType
   subType
   layoutId
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier.  """  
      pass

class ResetToDefaultLayout_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ShellLayoutTableset] = obj["returnObj"]
      pass

class SaveDataDiscoveryUrl_input:
   """ Required : 
   url
   """  
   def __init__(self, obj):
      self.url:str = obj["url"]
      """  The URL.  """  
      pass

class SaveDataDiscoveryUrl_output:
   def __init__(self, obj):
      pass

class SaveImageForTile_input:
   """ Required : 
   fileName
   imageBlob
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      """  Name of the file.  """  
      self.imageBlob:str = obj["imageBlob"]
      """  The image BLOB.  """  
      pass

class SaveImageForTile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class SaveShellLayoutAsPersonal_input:
   """ Required : 
   homePageType
   subType
   layoutId
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier. Pass in empty string for modern.  """  
      pass

class SaveShellLayoutAsPersonal_output:
   def __init__(self, obj):
      pass

class SelectPublishedLayoutForUser_input:
   """ Required : 
   publishedLayoutId
   homePageType
   subType
   replaceFavorites
   """  
   def __init__(self, obj):
      self.publishedLayoutId:str = obj["publishedLayoutId"]
      """  The published layout identifier.  """  
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      self.replaceFavorites:bool = obj["replaceFavorites"]
      """  if set to `true` replaces the favorites for the current user.  """  
      pass

class SelectPublishedLayoutForUser_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ShellLayoutTableset] = obj["returnObj"]
      pass

class SetAsSystemDefaultLayout_input:
   """ Required : 
   publishedLayout
   homePageType
   subType
   """  
   def __init__(self, obj):
      self.publishedLayout:str = obj["publishedLayout"]
      """  The layout identifier. Send in null if IsHomeDefault should be reset.  """  
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      pass

class SetAsSystemDefaultLayout_output:
   def __init__(self, obj):
      pass

class UnpublishLayout_input:
   """ Required : 
   publishedLayoutId
   homePageType
   subType
   """  
   def __init__(self, obj):
      self.publishedLayoutId:str = obj["publishedLayoutId"]
      """  The published layout identifier.  """  
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      pass

class UnpublishLayout_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtShellLayoutTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtShellLayoutTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateHomePageForUser_input:
   """ Required : 
   homePageType
   subType
   layoutId
   homePageData
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  Type of the sub.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier. Empty string for 'modern'. 'Default' or user defined layout identifier in kinetic.  """  
      self.homePageData:list[Ice_Tablesets_HomePageTableset] = obj["homePageData"]
      pass

class UpdateHomePageForUser_output:
   def __init__(self, obj):
      pass

class UpdateSecurityCodeForPublishedLayout_input:
   """ Required : 
   publishedLayoutId
   newSecurityCode
   homePageType
   subType
   """  
   def __init__(self, obj):
      self.publishedLayoutId:str = obj["publishedLayoutId"]
      """  The published layout identifier.  """  
      self.newSecurityCode:str = obj["newSecurityCode"]
      """  The new security code.  """  
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  The client side implementation, 'modern' or 'kinetic'.  """  
      pass

class UpdateSecurityCodeForPublishedLayout_output:
   def __init__(self, obj):
      pass

class UpdateUserOptionsForUser_input:
   """ Required : 
   homePageType
   subType
   layoutId
   userOptionsData
   """  
   def __init__(self, obj):
      self.homePageType:str = obj["homePageType"]
      """  Type of the home page.  """  
      self.subType:str = obj["subType"]
      """  Type of the sub.  """  
      self.layoutId:str = obj["layoutId"]
      """  The layout identifier. Pass empty string for 'modern' subtype.  """  
      self.userOptionsData:list[Ice_Tablesets_UserOptionsTableset] = obj["userOptionsData"]
      pass

class UpdateUserOptionsForUser_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ShellLayoutTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ShellLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

