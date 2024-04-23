import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.MenuSvc
# Description: Identifies the menu items that are displayed on the main menu.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Menus(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Menus items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Menus
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MenuRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus",headers=creds) as resp:
           return await resp.json()

async def post_Menus(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Menus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.MenuRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.MenuRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Menus_Company_MenuID(Company, MenuID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Menu item
   Description: Calls GetByID to retrieve the Menu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Menu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MenuID: Desc: MenuID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MenuRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus(" + Company + "," + MenuID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Menus_Company_MenuID(Company, MenuID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Menu for the service
   Description: Calls UpdateExt to update Menu. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Menu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MenuID: Desc: MenuID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.MenuRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus(" + Company + "," + MenuID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Menus_Company_MenuID(Company, MenuID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Menu item
   Description: Call UpdateExt to delete Menu item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Menu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MenuID: Desc: MenuID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/Menus(" + Company + "," + MenuID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MenuListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMenu, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMenu=" + whereClauseMenu
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, menuID, epicorHeaders = None):
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
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "menuID=" + menuID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsTranslated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsTranslated
   Description: Gets translation for each existing Row
   OperationID: GetRowsTranslated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWebAccess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWebAccess
   Description: Gets Rows that that are accessible from the WEB
   OperationID: GetRowsWebAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWebAccess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWebAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMenuID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMenuID
   Description: Returns a DataSet given the primary key.
   OperationID: GetMenuID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMenuID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMenuID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWebAccessTranslated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWebAccessTranslated
   Description: Gets Rows that that are accessible from the WEB
   OperationID: GetRowsWebAccessTranslated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWebAccessTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWebAccessTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCRM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCRM
   Description: Gets Rows that that are accessible from the WEB
   OperationID: GetRowsCRM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCRM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCRM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCRMTranslated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCRMTranslated
   Description: Gets Rows that that are accessible from the WEB
   OperationID: GetRowsCRMTranslated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCRMTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCRMTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyBeforeMenuItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyBeforeMenuItem
   Description: Move or Copy one menu item (source) before another (Target)
   OperationID: CopyBeforeMenuItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyBeforeMenuItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyBeforeMenuItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyMenuRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyMenuRow
   Description: Copy an existing Menu to a new menu row
   OperationID: CopyMenuRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyMenuRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyMenuRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyToParentMenu(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyToParentMenu
   Description: Move or Copy one menu item to the last menu item of the parent
   OperationID: CopyToParentMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyToParentMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyToParentMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMenuForLicenseType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMenuForLicenseType
   Description: Gets the type of the menu for the license type that the client is running under.
   OperationID: GetMenuForLicenseType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMenuForLicenseType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMenuForLicenseType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMenuBeforeLaunch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMenuBeforeLaunch
   Description: Validates if the UI represented by the Url can be launched by calling an ERP menu extension.
   OperationID: ValidateMenuBeforeLaunch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMenuBeforeLaunch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMenuBeforeLaunch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMenuAllowedForUserByView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMenuAllowedForUserByView
   Description: Determines whether the user has access to a Menu based on the ViewID.
   OperationID: GetMenuAllowedForUserByView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMenuAllowedForUserByView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMenuAllowedForUserByView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckMenuSecurityForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckMenuSecurityForUser
   Description: Determines if the user has access to the given MenuID or ViewID
   OperationID: CheckMenuSecurityForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckMenuSecurityForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMenuSecurityForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GlobalRecordFound(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GlobalRecordFound
   OperationID: GlobalRecordFound
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GlobalRecordFound_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlobalRecordFound_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProgamFoundInMenu(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProgamFoundInMenu
   OperationID: ProgamFoundInMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProgamFoundInMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProgamFoundInMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetKineticCustomizations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetKineticCustomizations
   Description: Gets the kinetic customizations allowed for provided view.
   OperationID: GetKineticCustomizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetKineticCustomizations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKineticCustomizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetKineticViews(epicorHeaders = None):
   """  
   Summary: Invoke method GetKineticViews
   Description: Gets the kinetic views.
   OperationID: GetKineticViews
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKineticViews_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCompaniesKineticStatus(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompaniesKineticStatus
   Description: Lists all companies that the user has access to and whether Kinetic UI is enabled
   OperationID: GetCompaniesKineticStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompaniesKineticStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetBannerSnoozeDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBannerSnoozeDays
   Description: Gets the number of days the Kinetic alert to use new UI is not shown after the user "snoozes" it.
This setting is per company.
   OperationID: GetBannerSnoozeDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBannerSnoozeDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBannerSnoozeDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDefaultFormType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDefaultFormType
   Description: Update a menu default form type to the target type
   OperationID: UpdateDefaultFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDefaultFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDefaultFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnableKineticUIOnRelatedMenus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnableKineticUIOnRelatedMenus
   Description: Enable Kinetic UI on related menus
   OperationID: EnableKineticUIOnRelatedMenus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableKineticUIOnRelatedMenus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableKineticUIOnRelatedMenus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateKineticBannerSnooze(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateKineticBannerSnooze
   Description: Update the Kinetic Banner snooze duration
   OperationID: UpdateKineticBannerSnooze
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateKineticBannerSnooze_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateKineticBannerSnooze_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnableKineticUIForDynamicReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnableKineticUIForDynamicReport
   Description: Enables the Kinetic UI for a dynamic report menu item
   OperationID: EnableKineticUIForDynamicReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableKineticUIForDynamicReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableKineticUIForDynamicReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMenu(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMenu
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetModuleList(epicorHeaders = None):
   """  
   Summary: Invoke method GetModuleList
   Description: Create list of modules
   OperationID: GetModuleList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetModuleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CGCCodeList(epicorHeaders = None):
   """  
   Summary: Invoke method CGCCodeList
   Description: Build cgccode list.
   OperationID: CGCCodeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CGCCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRowsMenuMaint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsMenuMaint
   Description: Prepare menu row for editing
   OperationID: GetRowsMenuMaint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsMenuMaint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsMenuMaint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsMenuMaintCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsMenuMaintCustom
   Description: Support for searching menu.
   OperationID: GetRowsMenuMaintCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsMenuMaintCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsMenuMaintCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewMenu(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewMenu
   Description: Add a new menu with defaults
   OperationID: CreateNewMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTopLevelMenus(epicorHeaders = None):
   """  
   Summary: Invoke method GetTopLevelMenus
   Description: Return top level menus only if a security manager
   OperationID: GetTopLevelMenus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTopLevelMenus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_KineticPreviewEnabled(epicorHeaders = None):
   """  
   Summary: Invoke method KineticPreviewEnabled
   Description: Return true if Kinetic preview is enabled
   OperationID: KineticPreviewEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticPreviewEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: verify/Update menu fields before calling standard update event.  In place to handle code that was in the classic UI.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KineticChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KineticChanged
   Description: Update fields if Kinetic flag changes.
   OperationID: KineticChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KineticChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KineticProgamChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KineticProgamChanged
   Description: Update fields if Kinetic flag changes.
   OperationID: KineticProgamChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KineticProgamChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticProgamChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OptioTypeChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OptioTypeChanged
   Description: Update menu fields when field optionType is changed.
   OperationID: OptioTypeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OptioTypeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OptioTypeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BAQReportChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BAQReportChanging
   Description: Validate Dynamic Report
   OperationID: BAQReportChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BAQReportChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BAQReportChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DyanmicReportChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DyanmicReportChanging
   Description: Validate Dynamic Report
   OperationID: DyanmicReportChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DyanmicReportChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DyanmicReportChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MenuSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MenuListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MenuListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MenuRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MenuRow] = obj["value"]
      pass

class Ice_Tablesets_MenuListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MenuID:str = obj["MenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  Menu Description  """  
      self.ParentMenuID:str = obj["ParentMenuID"]
      """  Needs manual validation because you cannot do can-find validation on the same file in the database validation.  """  
      self.Sequence:int = obj["Sequence"]
      """  Menu Sequence Number  """  
      self.OptionType:str = obj["OptionType"]
      """   S = Sub Menu,
I = Menu Item (Program),
B = Report Builder Report Link  """  
      self.OptionSubType:str = obj["OptionSubType"]
      """   F = Form
T = Tracker
M = Maintenance
P = Process
R = Report
E = Entry  """  
      self.Program:str = obj["Program"]
      """  Either the path/program or the ID of the Custom Report Link to run.  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled flag  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  """  
      self.DoNotDisplayInMenu:bool = obj["DoNotDisplayInMenu"]
      """  If this field is YES, this menu item should not display in the Main Menu.  """  
      self.Arguments:str = obj["Arguments"]
      """  Arguments to be passed to the program that this menu item refers to (see field "Program").  """  
      self.Module:str = obj["Module"]
      """  Contains the licensing module that this menu item belongs to.  """  
      self.MenuType:str = obj["MenuType"]
      """  Indicates a menu group that menu item belongs to  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.DashboardID:str = obj["DashboardID"]
      """  The Dashboard ID  """  
      self.ExpressAvailable:bool = obj["ExpressAvailable"]
      """  Whether this menu item is available under the Express edition.  """  
      self.CRMMenu:bool = obj["CRMMenu"]
      """  CRMMenu  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WebResourceURL:str = obj["WebResourceURL"]
      """  WebResourceURL  """  
      self.DefaultFormType:str = obj["DefaultFormType"]
      """  DefaultFormType  """  
      self.Customization:str = obj["Customization"]
      """  Customization  """  
      self.Extension:str = obj["Extension"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.Options:str = obj["Options"]
      self.DeveloperMode:bool = obj["DeveloperMode"]
      self.Dashboard:str = obj["Dashboard"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MenuRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MenuID:str = obj["MenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  Menu Description  """  
      self.ParentMenuID:str = obj["ParentMenuID"]
      """  Needs manual validation because you cannot do can-find validation on the same file in the database validation.  """  
      self.Sequence:int = obj["Sequence"]
      """  Menu Sequence Number  """  
      self.OptionType:str = obj["OptionType"]
      """   S = Sub Menu,
I = Menu Item (Program),
B = Report Builder Report Link  """  
      self.OptionSubType:str = obj["OptionSubType"]
      """   F = Form
T = Tracker
M = Maintenance
P = Process
R = Report
E = Entry  """  
      self.Program:str = obj["Program"]
      """  Either the path/program or the ID of the Custom Report Link to run.  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled flag  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  """  
      self.DoNotDisplayInMenu:bool = obj["DoNotDisplayInMenu"]
      """  If this field is YES, this menu item should not display in the Main Menu.  """  
      self.Arguments:str = obj["Arguments"]
      """  Arguments to be passed to the program that this menu item refers to (see field "Program").  """  
      self.Module:str = obj["Module"]
      """  Contains the licensing module that this menu item belongs to.  """  
      self.MenuType:str = obj["MenuType"]
      """  Indicates a menu group that menu item belongs to  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.DashboardID:str = obj["DashboardID"]
      """  The Dashboard ID  """  
      self.ExpressAvailable:bool = obj["ExpressAvailable"]
      """  Whether this menu item is available under the Express edition.  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.OldProgram:str = obj["OldProgram"]
      """  OldProgram  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.CRMMenu:bool = obj["CRMMenu"]
      """  CRMMenu  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SaaSParam:str = obj["SaaSParam"]
      """  SaaSParam  """  
      self.WebResourceURL:str = obj["WebResourceURL"]
      """  WebResourceURL  """  
      self.DefaultFormType:str = obj["DefaultFormType"]
      """  DefaultFormType  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.RunOnClassic:bool = obj["RunOnClassic"]
      """  RunOnClassic  """  
      self.Dashboard:str = obj["Dashboard"]
      self.DeveloperMode:bool = obj["DeveloperMode"]
      self.Extension:str = obj["Extension"]
      self.Options:str = obj["Options"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.Customization:str = obj["Customization"]
      """  Customization  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.ShowWebNavBar:bool = obj["ShowWebNavBar"]
      """  Indicates if the navigation bar (forward/back/refresh) should be shown on the form if the Program Type is URL Form.  """  
      self.ValidateBeforeLaunch:bool = obj["ValidateBeforeLaunch"]
      """  Description: Indicates if menu will be validated additionally by business logic before being launched. Used by Kinetic menus.  """  
      self.CustomizationKinetic:str = obj["CustomizationKinetic"]
      self.CanModify:bool = obj["CanModify"]
      self.FormName:str = obj["FormName"]
      self.Kinetic:bool = obj["Kinetic"]
      self.ProgramKinetic:str = obj["ProgramKinetic"]
      """  Kinetic program  """  
      self.CustomizationType:str = obj["CustomizationType"]
      """  Customization Type  """  
      self.Select:bool = obj["Select"]
      self.IsDuplicate:bool = obj["IsDuplicate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BAQReportChanging_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class BAQReportChanging_output:
   def __init__(self, obj):
      pass

class CGCCodeList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class CheckMenuSecurityForUser_input:
   """ Required : 
   viewId
   menuId
   """  
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      """  View ID to check for.  """  
      self.menuId:str = obj["menuId"]
      """  Menu ID to check for.  """  
      pass

class CheckMenuSecurityForUser_output:
   def __init__(self, obj):
      pass

class CopyBeforeMenuItem_input:
   """ Required : 
   sourceMenuID
   targetMenuID
   """  
   def __init__(self, obj):
      self.sourceMenuID:str = obj["sourceMenuID"]
      """  Menu ID of the source  """  
      self.targetMenuID:str = obj["targetMenuID"]
      """  Menu ID of the target  """  
      pass

class CopyBeforeMenuItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newMenuID:str = obj["parameters"]
      self.bSuccess:bool = obj["bSuccess"]
      pass

      """  output parameters  """  

class CopyMenuRow_input:
   """ Required : 
   ds
   sourceCompany
   sourceMenuID
   targetCompany
   targetMenuID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      self.sourceCompany:str = obj["sourceCompany"]
      """  Existing Menu Company  """  
      self.sourceMenuID:str = obj["sourceMenuID"]
      """  Existing Menu ID of the source  """  
      self.targetCompany:str = obj["targetCompany"]
      """  new menu company  """  
      self.targetMenuID:str = obj["targetMenuID"]
      """  new menu ID  """  
      pass

class CopyMenuRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopyToParentMenu_input:
   """ Required : 
   sourceMenuID
   parentMenuID
   """  
   def __init__(self, obj):
      self.sourceMenuID:str = obj["sourceMenuID"]
      """  Menu ID of the source  """  
      self.parentMenuID:str = obj["parentMenuID"]
      """  Menu ID of the parent  """  
      pass

class CopyToParentMenu_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newMenuID:str = obj["parameters"]
      self.bSuccess:bool = obj["bSuccess"]
      pass

      """  output parameters  """  

class CreateNewMenu_input:
   """ Required : 
   ds
   parentCompany
   parrentMenuId
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      self.parentCompany:str = obj["parentCompany"]
      self.parrentMenuId:str = obj["parrentMenuId"]
      pass

class CreateNewMenu_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   company
   menuID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.menuID:str = obj["menuID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DyanmicReportChanging_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class DyanmicReportChanging_output:
   def __init__(self, obj):
      pass

class EnableKineticUIForDynamicReport_input:
   """ Required : 
   reportId
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report id  """  
      pass

class EnableKineticUIForDynamicReport_output:
   def __init__(self, obj):
      pass

class EnableKineticUIOnRelatedMenus_input:
   """ Required : 
   company
   menuIDs
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.menuIDs:str = obj["menuIDs"]
      """  Menu IDs to search with  """  
      pass

class EnableKineticUIOnRelatedMenus_output:
   def __init__(self, obj):
      pass

class GetBannerSnoozeDays_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  the company  """  
      pass

class GetBannerSnoozeDays_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  the number of days to snooze the alert.  """  
      pass

class GetByID_input:
   """ Required : 
   company
   menuID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.menuID:str = obj["menuID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

class GetCompaniesKineticStatus_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  List of company, name and Kinetic feature flag enabled  """  
      pass

class GetKineticCustomizations_input:
   """ Required : 
   viewId
   """  
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      """  The view identifier.  """  
      pass

class GetKineticCustomizations_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of customizations delimited. Example: LayerName`Layer Description~LayerName2`Layer Description 2  """  
      pass

class GetKineticViews_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The kinetic views available.  """  
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
      self.returnObj:list[Ice_Tablesets_MenuListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMenuAllowedForUserByView_input:
   """ Required : 
   viewId
   """  
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      """  View ID to check for.  """  
      pass

class GetMenuAllowedForUserByView_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

class GetMenuForLicenseType_input:
   """ Required : 
   licenseType
   filterForWebAccess
   filterKineticOnly
   """  
   def __init__(self, obj):
      self.licenseType:str = obj["licenseType"]
      """  Type of the license. Values: 'Default','CRM','TimeExpense'  """  
      self.filterForWebAccess:bool = obj["filterForWebAccess"]
      """  if set to `true` filters the menu items not available in Web Access.  """  
      self.filterKineticOnly:bool = obj["filterKineticOnly"]
      """  if set to `true` filters the menu items which are not Kinetic (called when in browser with no EWA)  """  
      pass

class GetMenuForLicenseType_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

class GetMenuID_input:
   """ Required : 
   menuID
   """  
   def __init__(self, obj):
      self.menuID:str = obj["menuID"]
      pass

class GetMenuID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

class GetModuleList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetNewMenu_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewMenu_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCRMTranslated_input:
   """ Required : 
   whereClauseMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMenu:str = obj["whereClauseMenu"]
      """  whereClauseSetupGrp">Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned. 0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsCRMTranslated_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCRM_input:
   """ Required : 
   whereClauseMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMenu:str = obj["whereClauseMenu"]
      """  whereClauseSetupGrp">Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned. 0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsCRM_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsMenuMaintCustom_input:
   """ Required : 
   whereClauseMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMenu:str = obj["whereClauseMenu"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsMenuMaintCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsMenuMaint_input:
   """ Required : 
   whereClauseMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMenu:str = obj["whereClauseMenu"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsMenuMaint_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsTranslated_input:
   """ Required : 
   whereClauseMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMenu:str = obj["whereClauseMenu"]
      """  whereClauseSetupGrp">Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned. 0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsTranslated_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsWebAccessTranslated_input:
   """ Required : 
   whereClauseMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMenu:str = obj["whereClauseMenu"]
      """  whereClauseSetupGrp">Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned. 0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsWebAccessTranslated_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsWebAccess_input:
   """ Required : 
   whereClauseMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMenu:str = obj["whereClauseMenu"]
      """  whereClauseSetupGrp">Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned. 0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsWebAccess_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMenu:str = obj["whereClauseMenu"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTopLevelMenus_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MenuListTableset] = obj["returnObj"]
      pass

class GlobalRecordFound_input:
   """ Required : 
   MenuID
   """  
   def __init__(self, obj):
      self.MenuID:str = obj["MenuID"]
      pass

class GlobalRecordFound_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.Company:str = obj["parameters"]
      self.CompanyVisibility:int = obj["parameters"]
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

class Ice_Tablesets_MenuListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MenuID:str = obj["MenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  Menu Description  """  
      self.ParentMenuID:str = obj["ParentMenuID"]
      """  Needs manual validation because you cannot do can-find validation on the same file in the database validation.  """  
      self.Sequence:int = obj["Sequence"]
      """  Menu Sequence Number  """  
      self.OptionType:str = obj["OptionType"]
      """   S = Sub Menu,
I = Menu Item (Program),
B = Report Builder Report Link  """  
      self.OptionSubType:str = obj["OptionSubType"]
      """   F = Form
T = Tracker
M = Maintenance
P = Process
R = Report
E = Entry  """  
      self.Program:str = obj["Program"]
      """  Either the path/program or the ID of the Custom Report Link to run.  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled flag  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  """  
      self.DoNotDisplayInMenu:bool = obj["DoNotDisplayInMenu"]
      """  If this field is YES, this menu item should not display in the Main Menu.  """  
      self.Arguments:str = obj["Arguments"]
      """  Arguments to be passed to the program that this menu item refers to (see field "Program").  """  
      self.Module:str = obj["Module"]
      """  Contains the licensing module that this menu item belongs to.  """  
      self.MenuType:str = obj["MenuType"]
      """  Indicates a menu group that menu item belongs to  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.DashboardID:str = obj["DashboardID"]
      """  The Dashboard ID  """  
      self.ExpressAvailable:bool = obj["ExpressAvailable"]
      """  Whether this menu item is available under the Express edition.  """  
      self.CRMMenu:bool = obj["CRMMenu"]
      """  CRMMenu  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WebResourceURL:str = obj["WebResourceURL"]
      """  WebResourceURL  """  
      self.DefaultFormType:str = obj["DefaultFormType"]
      """  DefaultFormType  """  
      self.Customization:str = obj["Customization"]
      """  Customization  """  
      self.Extension:str = obj["Extension"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.Options:str = obj["Options"]
      self.DeveloperMode:bool = obj["DeveloperMode"]
      self.Dashboard:str = obj["Dashboard"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MenuListTableset:
   def __init__(self, obj):
      self.MenuList:list[Ice_Tablesets_MenuListRow] = obj["MenuList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_MenuRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MenuID:str = obj["MenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  Menu Description  """  
      self.ParentMenuID:str = obj["ParentMenuID"]
      """  Needs manual validation because you cannot do can-find validation on the same file in the database validation.  """  
      self.Sequence:int = obj["Sequence"]
      """  Menu Sequence Number  """  
      self.OptionType:str = obj["OptionType"]
      """   S = Sub Menu,
I = Menu Item (Program),
B = Report Builder Report Link  """  
      self.OptionSubType:str = obj["OptionSubType"]
      """   F = Form
T = Tracker
M = Maintenance
P = Process
R = Report
E = Entry  """  
      self.Program:str = obj["Program"]
      """  Either the path/program or the ID of the Custom Report Link to run.  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled flag  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  """  
      self.DoNotDisplayInMenu:bool = obj["DoNotDisplayInMenu"]
      """  If this field is YES, this menu item should not display in the Main Menu.  """  
      self.Arguments:str = obj["Arguments"]
      """  Arguments to be passed to the program that this menu item refers to (see field "Program").  """  
      self.Module:str = obj["Module"]
      """  Contains the licensing module that this menu item belongs to.  """  
      self.MenuType:str = obj["MenuType"]
      """  Indicates a menu group that menu item belongs to  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.DashboardID:str = obj["DashboardID"]
      """  The Dashboard ID  """  
      self.ExpressAvailable:bool = obj["ExpressAvailable"]
      """  Whether this menu item is available under the Express edition.  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.OldProgram:str = obj["OldProgram"]
      """  OldProgram  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.CRMMenu:bool = obj["CRMMenu"]
      """  CRMMenu  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SaaSParam:str = obj["SaaSParam"]
      """  SaaSParam  """  
      self.WebResourceURL:str = obj["WebResourceURL"]
      """  WebResourceURL  """  
      self.DefaultFormType:str = obj["DefaultFormType"]
      """  DefaultFormType  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.RunOnClassic:bool = obj["RunOnClassic"]
      """  RunOnClassic  """  
      self.Dashboard:str = obj["Dashboard"]
      self.DeveloperMode:bool = obj["DeveloperMode"]
      self.Extension:str = obj["Extension"]
      self.Options:str = obj["Options"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.Customization:str = obj["Customization"]
      """  Customization  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.ShowWebNavBar:bool = obj["ShowWebNavBar"]
      """  Indicates if the navigation bar (forward/back/refresh) should be shown on the form if the Program Type is URL Form.  """  
      self.ValidateBeforeLaunch:bool = obj["ValidateBeforeLaunch"]
      """  Description: Indicates if menu will be validated additionally by business logic before being launched. Used by Kinetic menus.  """  
      self.CustomizationKinetic:str = obj["CustomizationKinetic"]
      self.CanModify:bool = obj["CanModify"]
      self.FormName:str = obj["FormName"]
      self.Kinetic:bool = obj["Kinetic"]
      self.ProgramKinetic:str = obj["ProgramKinetic"]
      """  Kinetic program  """  
      self.CustomizationType:str = obj["CustomizationType"]
      """  Customization Type  """  
      self.Select:bool = obj["Select"]
      self.IsDuplicate:bool = obj["IsDuplicate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MenuTableset:
   def __init__(self, obj):
      self.Menu:list[Ice_Tablesets_MenuRow] = obj["Menu"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtMenuTableset:
   def __init__(self, obj):
      self.Menu:list[Ice_Tablesets_MenuRow] = obj["Menu"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class KineticChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

class KineticChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

class KineticPreviewEnabled_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class KineticProgamChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

class KineticProgamChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OptioTypeChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

class OptioTypeChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProgamFoundInMenu_input:
   """ Required : 
   program
   """  
   def __init__(self, obj):
      self.program:str = obj["program"]
      """  program to look for  """  
      pass

class ProgamFoundInMenu_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.menuID:str = obj["parameters"]
      self.menuAdded:bool = obj["menuAdded"]
      pass

      """  output parameters  """  

class UpdateDefaultFormType_input:
   """ Required : 
   company
   menuID
   recursive
   defaultFormType
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company to target  """  
      self.menuID:str = obj["menuID"]
      """  Menu ID to start at  """  
      self.recursive:bool = obj["recursive"]
      """  Whether to recursively update child menu items  """  
      self.defaultFormType:str = obj["defaultFormType"]
      """  Default form type to assign  """  
      pass

class UpdateDefaultFormType_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtMenuTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtMenuTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateKineticBannerSnooze_input:
   """ Required : 
   company
   days
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company to target  """  
      self.days:int = obj["days"]
      """  Number of days to snooze  """  
      pass

class UpdateKineticBannerSnooze_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateMenuBeforeLaunch_input:
   """ Required : 
   viewId
   menuId
   """  
   def __init__(self, obj):
      self.viewId:str = obj["viewId"]
      """  View identifier for the UI form  """  
      self.menuId:str = obj["menuId"]
      """  Menu identifier for the UI form  """  
      pass

class ValidateMenuBeforeLaunch_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  False if UI should not be launched.  """  
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

