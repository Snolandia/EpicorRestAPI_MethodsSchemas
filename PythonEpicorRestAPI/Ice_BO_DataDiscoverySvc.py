import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.DataDiscoverySvc
# Description: DataDiscovery service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DataDiscoveries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataDiscoveries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataDiscoveries
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.EDDUserFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/DataDiscoveries",headers=creds) as resp:
           return await resp.json()

async def post_DataDiscoveries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataDiscoveries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.EDDUserFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.EDDUserFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/DataDiscoveries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataDiscoveries_UserID(UserID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataDiscovery item
   Description: Calls GetByID to retrieve the DataDiscovery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataDiscovery
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EDDUserFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/DataDiscoveries(" + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataDiscoveries_UserID(UserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataDiscovery for the service
   Description: Calls UpdateExt to update DataDiscovery. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataDiscovery
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.EDDUserFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/DataDiscoveries(" + UserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataDiscoveries_UserID(UserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataDiscovery item
   Description: Call UpdateExt to delete DataDiscovery item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataDiscovery
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/DataDiscoveries(" + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataDiscoveries_UserID_EDDUserComps(UserID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EDDUserComps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EDDUserComps1
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.EDDUserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/DataDiscoveries(" + UserID + ")/EDDUserComps",headers=creds) as resp:
           return await resp.json()

async def get_DataDiscoveries_UserID_EDDUserComps_UserID_Company(UserID, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EDDUserComp item
   Description: Calls GetByID to retrieve the EDDUserComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EDDUserComp1
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EDDUserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/DataDiscoveries(" + UserID + ")/EDDUserComps(" + UserID + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_EDDUserComps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EDDUserComps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EDDUserComps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.EDDUserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/EDDUserComps",headers=creds) as resp:
           return await resp.json()

async def post_EDDUserComps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EDDUserComps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.EDDUserCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.EDDUserCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/EDDUserComps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EDDUserComps_UserID_Company(UserID, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EDDUserComp item
   Description: Calls GetByID to retrieve the EDDUserComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EDDUserComp
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EDDUserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/EDDUserComps(" + UserID + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EDDUserComps_UserID_Company(UserID, Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EDDUserComp for the service
   Description: Calls UpdateExt to update EDDUserComp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EDDUserComp
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.EDDUserCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/EDDUserComps(" + UserID + "," + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EDDUserComps_UserID_Company(UserID, Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EDDUserComp item
   Description: Call UpdateExt to delete EDDUserComp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EDDUserComp
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/EDDUserComps(" + UserID + "," + Company + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.EDDUserFileListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseEDDUserFile, whereClauseEDDUserComp, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseEDDUserFile=" + whereClauseEDDUserFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEDDUserComp=" + whereClauseEDDUserComp
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(userID, epicorHeaders = None):
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
   params += "userID=" + userID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetEddUserInformation(epicorHeaders = None):
   """  
   Summary: Invoke method GetEddUserInformation
   Description: Uses the security credentials to retrieve the UserFile record
   OperationID: GetEddUserInformation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEddUserInformation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCompanyList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanyList
   Description: Gets the list of Companies
   OperationID: GetCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDataDiscoveryUrl(epicorHeaders = None):
   """  
   Summary: Invoke method GetDataDiscoveryUrl
   Description: Gets the DataDiscovery Url and validates the EDD application state is Online
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SaveDataDiscoveryUrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveDataDiscoveryUrl
   Description: Saves the data discovery url and creates Menu Row
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveDashboardChartView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveDashboardChartView
   Description: Save the dashboard chart view
   OperationID: SaveDashboardChartView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveDashboardChartView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDashboardChartView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetChartType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetChartType
   Description: Get chat type based on chart name
   OperationID: GetChartType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChartType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChartType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEDDUserFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEDDUserFile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEDDUserFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEDDUserFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEDDUserFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEDDUserComp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEDDUserComp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEDDUserComp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEDDUserComp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEDDUserComp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DataDiscoverySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_EDDUserCompRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_EDDUserCompRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_EDDUserFileListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_EDDUserFileListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_EDDUserFileRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_EDDUserFileRow] = obj["value"]
      pass

class Ice_Tablesets_EDDUserCompRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EDDUserFileListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EDDUserFileRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.Name:str = obj["Name"]
      """  User Name  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  User's email address.  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account has security maintenance privileges.  """  
      self.CurComp:str = obj["CurComp"]
      """  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  """  
      self.GroupList:str = obj["GroupList"]
      """  List of security groups the user belongs to.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PwdChangeRequestOn:str = obj["PwdChangeRequestOn"]
      """  PwdChangeRequestOn  """  
      self.ExternalIdentity:str = obj["ExternalIdentity"]
      """  ExternalIdentity  """  
      self.SSRSReportDesigner:bool = obj["SSRSReportDesigner"]
      """  SSRSReportDesigner  """  
      self.DefaultHomepageLayoutID:str = obj["DefaultHomepageLayoutID"]
      """  DefaultHomepageLayoutID  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.IoTUser:bool = obj["IoTUser"]
      """  IoTUser  """  
      self.IoTAdministrator:bool = obj["IoTAdministrator"]
      """  IoTAdministrator  """  
      self.DMTUser:bool = obj["DMTUser"]
      """  DMTUser  """  
      self.EVAUser:bool = obj["EVAUser"]
      """  EVAUser  """  
      self.DefaultFormType:str = obj["DefaultFormType"]
      """  DefaultFormType  """  
      self.HideKineticToast:bool = obj["HideKineticToast"]
      """  HideKineticToast  """  
      self.RestrictIP:bool = obj["RestrictIP"]
      """  RestrictIP  """  
      self.InstallationID:str = obj["InstallationID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.Character01:str = obj["Character01"]
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.SendSaaSAlert_c:bool = obj["SendSaaSAlert_c"]
      self.TempEpiSupportUser_c:bool = obj["TempEpiSupportUser_c"]
      self.EpicUpgrade_c:bool = obj["EpicUpgrade_c"]
      self.DisableDate_c:str = obj["DisableDate_c"]
      self.DisabledDate_c:str = obj["DisabledDate_c"]
      self.Checkbox20:bool = obj["Checkbox20"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DataDiscoveryTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DataDiscoveryTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DataDiscoveryTableset] = obj["returnObj"]
      pass

class GetChartType_input:
   """ Required : 
   chartName
   """  
   def __init__(self, obj):
      self.chartName:str = obj["chartName"]
      pass

class GetChartType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCompanyList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_DataDiscovery_CompanyListInfo] = obj["returnObj"]
      """  the list of Companies  """  
      pass

class GetDataDiscoveryUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The DataDiscovery Url when EDD application state is online  """  
      pass

class GetEddUserInformation_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DataDiscoveryTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DataDiscoveryListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEDDUserComp_input:
   """ Required : 
   ds
   userID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DataDiscoveryTableset] = obj["ds"]
      self.userID:str = obj["userID"]
      pass

class GetNewEDDUserComp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DataDiscoveryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEDDUserFile_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DataDiscoveryTableset] = obj["ds"]
      pass

class GetNewEDDUserFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DataDiscoveryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseEDDUserFile
   whereClauseEDDUserComp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseEDDUserFile:str = obj["whereClauseEDDUserFile"]
      self.whereClauseEDDUserComp:str = obj["whereClauseEDDUserComp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DataDiscoveryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BO_DataDiscovery_CompanyListInfo:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Name:str = obj["Name"]
      self.EwaUrl:str = obj["EwaUrl"]
      pass

class Ice_BO_DataDiscovery_EddChartFilter:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.Condition:str = obj["Condition"]
      self.Value:str = obj["Value"]
      self.IsValueAnotherColumn:bool = obj["IsValueAnotherColumn"]
      pass

class Ice_BO_DataDiscovery_EddDashboardChart:
   def __init__(self, obj):
      self.Id:str = obj["Id"]
      self.BAQ:str = obj["BAQ"]
      self.XAxis:str = obj["XAxis"]
      self.YAxis:str = obj["YAxis"]
      self.ZAxis:str = obj["ZAxis"]
      self.Filters:list[Ice_BO_DataDiscovery_EddChartFilter] = obj["Filters"]
      self.ChartType:str = obj["ChartType"]
      self.ChartCaption:str = obj["ChartCaption"]
      self.DashboardDefinitionID:str = obj["DashboardDefinitionID"]
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

class Ice_Tablesets_DataDiscoveryListTableset:
   def __init__(self, obj):
      self.EDDUserFileList:list[Ice_Tablesets_EDDUserFileListRow] = obj["EDDUserFileList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_DataDiscoveryTableset:
   def __init__(self, obj):
      self.EDDUserFile:list[Ice_Tablesets_EDDUserFileRow] = obj["EDDUserFile"]
      self.EDDUserComp:list[Ice_Tablesets_EDDUserCompRow] = obj["EDDUserComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_EDDUserCompRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EDDUserFileListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EDDUserFileRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.Name:str = obj["Name"]
      """  User Name  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  User's email address.  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account has security maintenance privileges.  """  
      self.CurComp:str = obj["CurComp"]
      """  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  """  
      self.GroupList:str = obj["GroupList"]
      """  List of security groups the user belongs to.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PwdChangeRequestOn:str = obj["PwdChangeRequestOn"]
      """  PwdChangeRequestOn  """  
      self.ExternalIdentity:str = obj["ExternalIdentity"]
      """  ExternalIdentity  """  
      self.SSRSReportDesigner:bool = obj["SSRSReportDesigner"]
      """  SSRSReportDesigner  """  
      self.DefaultHomepageLayoutID:str = obj["DefaultHomepageLayoutID"]
      """  DefaultHomepageLayoutID  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.IoTUser:bool = obj["IoTUser"]
      """  IoTUser  """  
      self.IoTAdministrator:bool = obj["IoTAdministrator"]
      """  IoTAdministrator  """  
      self.DMTUser:bool = obj["DMTUser"]
      """  DMTUser  """  
      self.EVAUser:bool = obj["EVAUser"]
      """  EVAUser  """  
      self.DefaultFormType:str = obj["DefaultFormType"]
      """  DefaultFormType  """  
      self.HideKineticToast:bool = obj["HideKineticToast"]
      """  HideKineticToast  """  
      self.RestrictIP:bool = obj["RestrictIP"]
      """  RestrictIP  """  
      self.InstallationID:str = obj["InstallationID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.Character01:str = obj["Character01"]
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.SendSaaSAlert_c:bool = obj["SendSaaSAlert_c"]
      self.TempEpiSupportUser_c:bool = obj["TempEpiSupportUser_c"]
      self.EpicUpgrade_c:bool = obj["EpicUpgrade_c"]
      self.DisableDate_c:str = obj["DisableDate_c"]
      self.DisabledDate_c:str = obj["DisabledDate_c"]
      self.Checkbox20:bool = obj["Checkbox20"]
      pass

class Ice_Tablesets_UpdExtDataDiscoveryTableset:
   def __init__(self, obj):
      self.EDDUserFile:list[Ice_Tablesets_EDDUserFileRow] = obj["EDDUserFile"]
      self.EDDUserComp:list[Ice_Tablesets_EDDUserCompRow] = obj["EDDUserComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class SaveDashboardChartView_input:
   """ Required : 
   dataDiscoveyURL
   dasboardChartSettings
   """  
   def __init__(self, obj):
      self.dataDiscoveyURL:str = obj["dataDiscoveyURL"]
      self.dasboardChartSettings:list[Ice_BO_DataDiscovery_EddDashboardChart] = obj["dasboardChartSettings"]
      pass

class SaveDashboardChartView_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class SaveDataDiscoveryUrl_input:
   """ Required : 
   url
   """  
   def __init__(self, obj):
      self.url:str = obj["url"]
      """  The data discovery url  """  
      pass

class SaveDataDiscoveryUrl_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDataDiscoveryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDataDiscoveryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DataDiscoveryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DataDiscoveryTableset] = obj["ds"]
      pass

      """  output parameters  """  

