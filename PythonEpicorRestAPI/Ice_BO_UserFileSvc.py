import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.UserFileSvc
# Description: User File Definition
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_UserFiles(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UserFiles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UserFiles
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles",headers=creds) as resp:
           return await resp.json()

async def post_UserFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UserFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UserFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UserFiles_UserID(UserID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserFile item
   Description: Calls GetByID to retrieve the UserFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserFile
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UserFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UserFiles_UserID(UserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UserFile for the service
   Description: Calls UpdateExt to update UserFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserFile
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UserFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UserFiles_UserID(UserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UserFile item
   Description: Call UpdateExt to delete UserFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserFile
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_UserFiles_UserID_UserComps(UserID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UserComps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UserComps1
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")/UserComps",headers=creds) as resp:
           return await resp.json()

async def get_UserFiles_UserID_UserComps_UserID_Company(UserID, Company, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserComp item
   Description: Calls GetByID to retrieve the UserComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserComp1
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")/UserComps(" + UserID + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_UserComps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UserComps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UserComps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps",headers=creds) as resp:
           return await resp.json()

async def post_UserComps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserComps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UserCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UserCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UserComps_UserID_Company(UserID, Company, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserComp item
   Description: Calls GetByID to retrieve the UserComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserComp
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UserComps_UserID_Company(UserID, Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UserComp for the service
   Description: Calls UpdateExt to update UserComp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserComp
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UserCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UserComps_UserID_Company(UserID, Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UserComp item
   Description: Call UpdateExt to delete UserComp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserComp
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_UserComps_UserID_Company_UserCompExts(UserID, Company, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UserCompExts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UserCompExts1
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserCompExtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")/UserCompExts",headers=creds) as resp:
           return await resp.json()

async def get_UserComps_UserID_Company_UserCompExts_UserID_Company_ExtCompID(UserID, Company, ExtCompID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserCompExt item
   Description: Calls GetByID to retrieve the UserCompExt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserCompExt1
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompID: Desc: ExtCompID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UserCompExtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")/UserCompExts(" + UserID + "," + Company + "," + ExtCompID + ")",headers=creds) as resp:
           return await resp.json()

async def get_UserCompExts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UserCompExts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UserCompExts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserCompExtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts",headers=creds) as resp:
           return await resp.json()

async def post_UserCompExts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserCompExts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UserCompExtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UserCompExtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UserCompExts_UserID_Company_ExtCompID(UserID, Company, ExtCompID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserCompExt item
   Description: Calls GetByID to retrieve the UserCompExt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserCompExt
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompID: Desc: ExtCompID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UserCompExtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts(" + UserID + "," + Company + "," + ExtCompID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UserCompExts_UserID_Company_ExtCompID(UserID, Company, ExtCompID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UserCompExt for the service
   Description: Calls UpdateExt to update UserCompExt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserCompExt
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompID: Desc: ExtCompID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UserCompExtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts(" + UserID + "," + Company + "," + ExtCompID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UserCompExts_UserID_Company_ExtCompID(UserID, Company, ExtCompID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UserCompExt item
   Description: Call UpdateExt to delete UserCompExt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserCompExt
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompID: Desc: ExtCompID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts(" + UserID + "," + Company + "," + ExtCompID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserFileListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseUserFile, whereClauseUserComp, whereClauseUserCompExt, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseUserFile=" + whereClauseUserFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUserComp=" + whereClauseUserComp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUserCompExt=" + whereClauseUserCompExt
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddUserCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddUserCompany
   Description: This method will create a new row in the UserComp data table related to the given UserID.
   OperationID: AddUserCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePassword(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePassword
   Description: Changes the specified user's password.
   OperationID: ChangePassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForCompany
   Description: This method is to be run when the user leaves the UserFile record. It will check to see that at least one
UserComp record exists. If not the user must add one before continuing on.
   OperationID: CheckForCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DetermineAccessibleInstallationsForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DetermineAccessibleInstallationsForUser
   Description: Determines the accessible installations for user.
   OperationID: DetermineAccessibleInstallationsForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DetermineAccessibleInstallationsForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DetermineAccessibleInstallationsForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUserFile(epicorHeaders = None):
   """  
   Summary: Invoke method GetUserFile
   Description: Uses the security credentials to retrieve the UserFile record
   OperationID: GetUserFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentUserId(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentUserId
   Description: Uses the security credentials to retrieve the current ERP user Id
   OperationID: GetCurrentUserId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentUserId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetExtCompanyList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExtCompanyList
   Description: Builds a list of the external companies for the specified company.
   OperationID: GetExtCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtCompanyList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveSettings
   Description: Save user settings.
Unlike the Update method, there is no optimistic locking performed.
So the settings are saved in a last in wins basis.
   OperationID: SaveSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsPasswordExpired(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsPasswordExpired
   Description: Check if password is expired.
   OperationID: IsPasswordExpired
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsPasswordExpired_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPasswordExpired_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePassword(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePassword
   Description: Check if password is valid.
   OperationID: ValidatePassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsUserIDAvailable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsUserIDAvailable
   Description: Check if user can be created with this UserID. Available for security managers
   OperationID: IsUserIDAvailable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsUserIDAvailable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsUserIDAvailable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExpireAllPasswords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExpireAllPasswords
   Description: Expire the passwords for all the users within the current tenant.
   OperationID: ExpireAllPasswords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireAllPasswords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireAllPasswords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockAccount
   Description: Unlocks the account for the user
   OperationID: UnlockAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AllowBlankPassword(epicorHeaders = None):
   """  
   Summary: Invoke method AllowBlankPassword
   Description: Is a blank Password Allowed
   OperationID: AllowBlankPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowBlankPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AccountDisabled(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AccountDisabled
   Description: Is a blank Password Allowed
   OperationID: AccountDisabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AccountDisabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AccountDisabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetPassword(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetPassword
   Description: Allows a temp password to be set.
   OperationID: ResetPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportUserToIdentityProvider(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportUserToIdentityProvider
   Description: Sends user information to Identity Provider
   OperationID: ExportUserToIdentityProvider
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportUserToIdentityProvider_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportUserToIdentityProvider_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BulkUserExportToIdentityProvider(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BulkUserExportToIdentityProvider
   Description: Bulk user export to Identity Provider
   OperationID: BulkUserExportToIdentityProvider
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkUserExportToIdentityProvider_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkUserExportToIdentityProvider_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCompanyFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCompanyFilter
   Description: Returns a list of user filtered by Company
   OperationID: GetListCompanyFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCompanyFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCompanyFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompanyListForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanyListForUser
   Description: Returns a list of the "visible" companies by the user (i.e. the companies in the same tenancy), or all if the user is a GSM.
   OperationID: GetCompanyListForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCompanyListForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyListForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableCompanyListForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableCompanyListForUser
   Description: Returns a list of the "available" companies by the user (i.e. the companies in the same tenancy), or all if the user is a GSM.
   OperationID: GetAvailableCompanyListForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableCompanyListForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableCompanyListForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BackupIdentities(epicorHeaders = None):
   """  
   Summary: Invoke method BackupIdentities
   Description: Backup user identity information to user data folder.
   OperationID: BackupIdentities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/BackupIdentities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_RestoreIdentities(epicorHeaders = None):
   """  
   Summary: Invoke method RestoreIdentities
   Description: Restore user identity information from user data folder and update user files.
   OperationID: RestoreIdentities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestoreIdentities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DeleteTemporaryFile(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteTemporaryFile
   Description: Deletes temporary file after downloading
   OperationID: DeleteTemporaryFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTemporaryFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentInstallationId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentInstallationId
   Description: Returns the InstallationId from SysCompany using the user's CurComp
   OperationID: GetCurrentInstallationId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentInstallationId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentInstallationId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUserFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUserFile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUserFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUserFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUserFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUserComp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUserComp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUserComp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUserComp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUserComp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUserCompExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUserCompExt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUserCompExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUserCompExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUserCompExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompExtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UserCompExtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UserCompRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserFileListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UserFileListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserFileRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UserFileRow] = obj["value"]
      pass

class Ice_Tablesets_UserCompExtRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      """  External Company ID  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdateExpense:bool = obj["CanUpdateExpense"]
      """  Indicates if the user can update expense entries (EmpExpense) for any employee.  """  
      self.CanUpdateTime:bool = obj["CanUpdateTime"]
      """  Indicates if the user can update time entries (LaborDtl) for any employee.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.WorkstationID:str = obj["WorkstationID"]
      """  Unique identifier of the Workstations  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanyName:str = obj["CompanyName"]
      self.UserIDName:str = obj["UserIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UserFileListRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.Name:str = obj["Name"]
      """  User Name  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country portion of the address  """  
      self.OfficePhone:str = obj["OfficePhone"]
      """  Office phone number  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  User's email address.  """  
      self.UserDisabled:bool = obj["UserDisabled"]
      """  Indicates if the user account has been disabled (turned off).  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account has security maintenance privileges.  """  
      self.CanChangeSaveSettings:bool = obj["CanChangeSaveSettings"]
      """  Allow user to change save settings  """  
      self.CurComp:str = obj["CurComp"]
      """  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  """  
      self.PwdLastChanged:str = obj["PwdLastChanged"]
      """  Date that the password was last changed.  """  
      self.PwdExpiresDays:int = obj["PwdExpiresDays"]
      """  Password expires x days after the password has been changed.  Zero means the password does not automatically expire.  """  
      self.PwdExpires:str = obj["PwdExpires"]
      """  The date that the user account password expires.  """  
      self.PwdGrace:int = obj["PwdGrace"]
      """  The number of remaining grace logins.  """  
      self.GroupList:str = obj["GroupList"]
      """  List of security groups the user belongs to.  """  
      self.CompList:str = obj["CompList"]
      """  List of companies the user has access to.  """  
      self.ViewFavoriteBar:bool = obj["ViewFavoriteBar"]
      """  Enable Favorite Bar  """  
      self.ViewStatusBar:bool = obj["ViewStatusBar"]
      """  Enable Status Bar  """  
      self.CurFolderSeq:int = obj["CurFolderSeq"]
      """  Sequence number of the folder in focus  """  
      self.CurMenuID:str = obj["CurMenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.DispTips:bool = obj["DispTips"]
      """  Indicates if the user wants tips to be displayed during logon.  """  
      self.CanChangePassword:bool = obj["CanChangePassword"]
      """  Whether the user can change their password.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.LastGraphType:str = obj["LastGraphType"]
      """  The last type of Graph (Bar, 3D Bar, Line, etc.) used in the Schedule Load Graph program.  """  
      self.UseInternalWebBrowser:bool = obj["UseInternalWebBrowser"]
      """  Indicates that the internal web browser should be used instead of using the OS registered browser.  """  
      self.AllowMultipleSessions:bool = obj["AllowMultipleSessions"]
      """  Allow user to start multiple sessions at the same time.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates that the user has Web interface privileges.  When this is turned on, the write trigger maintains certain fields in the WebUser table.  If this is never turned on, a corresponding WebUser doesn't exist.  If this has been on, and is now turned off, the WebUser record is set to disabled, but not deleted.  """  
      self.ListViewMode:int = obj["ListViewMode"]
      """  This property determines the viewing mode of the ListView object. The ListView object supports viewing items in four different modes: Icon(0),SmallIcon(1), List(2) and Report(3). Only 0 1 and 3 are used  """  
      self.CanMaintainFavQueries:bool = obj["CanMaintainFavQueries"]
      """  Whether the user can add/maintain Dashboard Queries on the favorites bar.  """  
      self.CanMaintainFavURLs:bool = obj["CanMaintainFavURLs"]
      """  Whether the user can add/maintain Dashboard URLs on the favorites bar.  """  
      self.CanMaintainFavPrograms:bool = obj["CanMaintainFavPrograms"]
      """  Whether the user can add/maintain Windows Programs on the favorites bar.  """  
      self.CanCustomize:bool = obj["CanCustomize"]
      """  Whether the user can access customization screens.  """  
      self.ViewTreeOnly:int = obj["ViewTreeOnly"]
      """  Whether to display the TreeView alone.  """  
      self.Timeout:int = obj["Timeout"]
      """  Time Out  """  
      self.CanPersonalize:bool = obj["CanPersonalize"]
      """  Whether the user can personalize.  """  
      self.CanTranslate:bool = obj["CanTranslate"]
      """  Whether the user can translate.  """  
      self.CanEditCompAnnotations:bool = obj["CanEditCompAnnotations"]
      """  Can this user edit Company level Help Annotations  """  
      self.CanEditUserAnnotations:bool = obj["CanEditUserAnnotations"]
      """  Can this user edit user level Help Annotations  """  
      self.CanEditHelpLinks:str = obj["CanEditHelpLinks"]
      """  Does this user get access to the HelpLink Editor  """  
      self.AutoStartMonitor:bool = obj["AutoStartMonitor"]
      """  Does this user want the Monitor to Started when they log in. (replaces Config Setting)  """  
      self.MonitorPollingInterval:int = obj["MonitorPollingInterval"]
      """  How frequently (expressed as secounds) the Monitor will poll for results  """  
      self.FormOpenMode:str = obj["FormOpenMode"]
      """  Default form open behavior (Nil, Auto'S'earch, Auto'P'opulate) -  (Replaces Config Setting)  """  
      self.EntConType:str = obj["EntConType"]
      """  Enterprise Connection Type, Determines how the UI Behaves when Session information is changed and UI forms are already present (Nil, 'S'ingleSession, 'M'ultiSession) (Replaces Config Setting)  """  
      self.DashboardDeveloper:bool = obj["DashboardDeveloper"]
      """  Allow user to open dashboards in developer mode  """  
      self.GlbCompSM:bool = obj["GlbCompSM"]
      """   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  """  
      self.LastLogOnAttempt:str = obj["LastLogOnAttempt"]
      """  LastLogOnAttempt  """  
      self.ThemeID:str = obj["ThemeID"]
      """  ThemeID  """  
      self.DisableTheming:bool = obj["DisableTheming"]
      """  DisableTheming  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalIdentity:str = obj["ExternalIdentity"]
      """  ExternalIdentity  """  
      self.SSRSReportDesigner:bool = obj["SSRSReportDesigner"]
      """  SSRSReportDesigner  """  
      self.RestrictIP:bool = obj["RestrictIP"]
      """  RestrictIP  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UserFileRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.Name:str = obj["Name"]
      """  User Name  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country portion of the address  """  
      self.OfficePhone:str = obj["OfficePhone"]
      """  Office phone number  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  User's email address.  """  
      self.UserDisabled:bool = obj["UserDisabled"]
      """  Indicates if the user account has been disabled (turned off).  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account has security maintenance privileges.  """  
      self.CanChangeSaveSettings:bool = obj["CanChangeSaveSettings"]
      """  Allow user to change save settings  """  
      self.SaveSettings:bool = obj["SaveSettings"]
      """  Save settings  """  
      self.CurComp:str = obj["CurComp"]
      """  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  """  
      self.PwdLastChanged:str = obj["PwdLastChanged"]
      """  Date that the password was last changed.  """  
      self.PwdExpiresDays:int = obj["PwdExpiresDays"]
      """  Password expires x days after the password has been changed.  Zero means the password does not automatically expire.  """  
      self.PwdExpires:str = obj["PwdExpires"]
      """  The date that the user account password expires.  """  
      self.PwdGrace:int = obj["PwdGrace"]
      """  The number of remaining grace logins.  """  
      self.GroupList:str = obj["GroupList"]
      """  List of security groups the user belongs to.  """  
      self.CompList:str = obj["CompList"]
      """  List of companies the user has access to.  """  
      self.ViewFavoriteBar:bool = obj["ViewFavoriteBar"]
      """  Enable Favorite Bar  """  
      self.ViewStatusBar:bool = obj["ViewStatusBar"]
      """  Enable Status Bar  """  
      self.WinX:int = obj["WinX"]
      """  Main menu X-position  """  
      self.WinY:int = obj["WinY"]
      """  Main menu Y-position  """  
      self.CurFolderSeq:int = obj["CurFolderSeq"]
      """  Sequence number of the folder in focus  """  
      self.CurMenuID:str = obj["CurMenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.WinWidth:int = obj["WinWidth"]
      """  Main menu width  """  
      self.WinHeight:int = obj["WinHeight"]
      """  Main menu height  """  
      self.DispTips:bool = obj["DispTips"]
      """  Indicates if the user wants tips to be displayed during logon.  """  
      self.CanChangePassword:bool = obj["CanChangePassword"]
      """  Whether the user can change their password.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.LastGraphType:str = obj["LastGraphType"]
      """  The last type of Graph (Bar, 3D Bar, Line, etc.) used in the Schedule Load Graph program.  """  
      self.UseInternalWebBrowser:bool = obj["UseInternalWebBrowser"]
      """  Indicates that the internal web browser should be used instead of using the OS registered browser.  """  
      self.AllowMultipleSessions:bool = obj["AllowMultipleSessions"]
      """  Allow user to start multiple sessions at the same time.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates that the user has Web interface privileges.  When this is turned on, the write trigger maintains certain fields in the WebUser table.  If this is never turned on, a corresponding WebUser doesn't exist.  If this has been on, and is now turned off, the WebUser record is set to disabled, but not deleted.  """  
      self.ListViewMode:int = obj["ListViewMode"]
      """  This property determines the viewing mode of the ListView object. The ListView object supports viewing items in four different modes: Icon(0),SmallIcon(1), List(2) and Report(3). Only 0 1 and 3 are used  """  
      self.CanMaintainFavQueries:bool = obj["CanMaintainFavQueries"]
      """  Whether the user can add/maintain Dashboard Queries on the favorites bar.  """  
      self.CanMaintainFavURLs:bool = obj["CanMaintainFavURLs"]
      """  Whether the user can add/maintain Dashboard URLs on the favorites bar.  """  
      self.CanMaintainFavPrograms:bool = obj["CanMaintainFavPrograms"]
      """  Whether the user can add/maintain Windows Programs on the favorites bar.  """  
      self.CanCustomize:bool = obj["CanCustomize"]
      """  Whether the user can access customization screens.  """  
      self.ViewTreeOnly:int = obj["ViewTreeOnly"]
      """  Whether to display the TreeView alone.  """  
      self.Timeout:int = obj["Timeout"]
      """  Time Out  """  
      self.CanPersonalize:bool = obj["CanPersonalize"]
      """  Whether the user can personalize.  """  
      self.CanTranslate:bool = obj["CanTranslate"]
      """  Whether the user can translate.  """  
      self.CanEditCompAnnotations:bool = obj["CanEditCompAnnotations"]
      """  Can this user edit Company level Help Annotations  """  
      self.CanEditUserAnnotations:bool = obj["CanEditUserAnnotations"]
      """  Can this user edit user level Help Annotations  """  
      self.CanEditHelpLinks:str = obj["CanEditHelpLinks"]
      """  Does this user get access to the HelpLink Editor  """  
      self.AutoStartMonitor:bool = obj["AutoStartMonitor"]
      """  Does this user want the Monitor to Started when they log in. (replaces Config Setting)  """  
      self.MonitorPollingInterval:int = obj["MonitorPollingInterval"]
      """  How frequently (expressed as secounds) the Monitor will poll for results  """  
      self.FormOpenMode:str = obj["FormOpenMode"]
      """  Default form open behavior (Nil, Auto'S'earch, Auto'P'opulate) -  (Replaces Config Setting)  """  
      self.EntConType:str = obj["EntConType"]
      """  Enterprise Connection Type, Determines how the UI Behaves when Session information is changed and UI forms are already present (Nil, 'S'ingleSession, 'M'ultiSession) (Replaces Config Setting)  """  
      self.DashboardDeveloper:bool = obj["DashboardDeveloper"]
      """  Allow user to open dashboards in developer mode  """  
      self.CanDesignQSearch:bool = obj["CanDesignQSearch"]
      """  Allow user to design quick searches  """  
      self.RequireSso:bool = obj["RequireSso"]
      """   Whether single sign-on (SSO) is required to log on.
Select this check box to indicate that this user has to use his/her operating system (Windows, Unix, and so on) logon information as the logon for Vantage. 
Single Sign-On (SSO) is functionality that allows users to sign on (log in) to Vantage using the Login IDs and Passwords they use to log into their computer's operating system (for example Windows, Unix, Linux and so on). In other words, if SSO is enabled, users will not be presented with a Logon window when they click their Vantage icon; they will be taken directly to the application's main menu.  """  
      self.ViewStatusPanelUserID:bool = obj["ViewStatusPanelUserID"]
      """  Show User ID in status panel  """  
      self.ViewStatusPanelLanguage:bool = obj["ViewStatusPanelLanguage"]
      """  Show language in status panel  """  
      self.ViewStatusPanelCompany:bool = obj["ViewStatusPanelCompany"]
      """  Show current company in status panel  """  
      self.ViewStatusPanelPlant:bool = obj["ViewStatusPanelPlant"]
      """  Show current Site in status panel  """  
      self.ViewStatusPanelServer:bool = obj["ViewStatusPanelServer"]
      """  Show server name in status panel  """  
      self.ViewStatusPanelWorkstationID:bool = obj["ViewStatusPanelWorkstationID"]
      """  Show workstation in status panel  """  
      self.DomainName:str = obj["DomainName"]
      """  Name of the operating system domain into which this users logs in.  Used when Require Single Sign on is enabled.  """  
      self.BPMAdvancedUser:bool = obj["BPMAdvancedUser"]
      """  Determines whether the user is allowed to use advanced development features of Business Process Management.  The freeform editor requires knowledge of Progress 4GL programming and specific method operational working.  Typically freeform options are used by Epicor custom programming or experienced programmers for advanced techniques not available through the wizard-like interface.  """  
      self.MaxGroupsFavorites:int = obj["MaxGroupsFavorites"]
      """  Maximum number of favorite bar groups  """  
      self.MaxGroupsSystemMenu:int = obj["MaxGroupsSystemMenu"]
      """  Maximum number of system menus  """  
      self.OSUserID:str = obj["OSUserID"]
      """  Operating system user ID.  """  
      self.CanTheme:bool = obj["CanTheme"]
      """  Allow user to create themes  """  
      self.FormatCulture:str = obj["FormatCulture"]
      """  Culture format  """  
      self.CanUseEntSearch:bool = obj["CanUseEntSearch"]
      """  yes = the user can use enterprise searches  """  
      self.CanAccEpiEverywhere:bool = obj["CanAccEpiEverywhere"]
      """  Allow access to EWA  """  
      self.CanAcessMobile:bool = obj["CanAcessMobile"]
      """  Allow Acess to Mobile Office  """  
      self.StartMenuClient:str = obj["StartMenuClient"]
      """  Initial start Menu for the Client  """  
      self.StartMenuEWA:str = obj["StartMenuEWA"]
      """  Initial Start Menu ID for EWA  """  
      self.StartMenuMobile:str = obj["StartMenuMobile"]
      """  Initial Start Menu ID for Mobile  """  
      self.AdvBAQRights:bool = obj["AdvBAQRights"]
      """  Allow advanced BAQ designer rights  """  
      self.SecurityAccessOnly:bool = obj["SecurityAccessOnly"]
      """  Defines isthe uesr has Security Access Only  """  
      self.SolutionMgrCreate:bool = obj["SolutionMgrCreate"]
      """  Defines if is user can create a Solution using the Solution Manager  """  
      self.SolutionMgrInstall:bool = obj["SolutionMgrInstall"]
      """  Defines if a user can install Solutions using the Solution Manager  """  
      self.EntSearchURL:str = obj["EntSearchURL"]
      """  Enterprise Search URL  """  
      self.CanMaintQuickSearch:bool = obj["CanMaintQuickSearch"]
      """  Whether the user can add/maintain Quick Searches.  """  
      self.UseDefaultEntSearch:bool = obj["UseDefaultEntSearch"]
      """  Use Default Enterprise Search  """  
      self.UserAccessOnly:bool = obj["UserAccessOnly"]
      """  UserAccessOnly  """  
      self.GlbCompSM:bool = obj["GlbCompSM"]
      """   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  """  
      self.BAQXCompany:bool = obj["BAQXCompany"]
      """  BAQXCompany  """  
      self.LastLogOnAttempt:str = obj["LastLogOnAttempt"]
      """  LastLogOnAttempt  """  
      self.CanImpersonate:bool = obj["CanImpersonate"]
      """  CanImpersonate  """  
      self.ViewStatusPanelSolutionID:bool = obj["ViewStatusPanelSolutionID"]
      """  ViewStatusPanelSolutionID  """  
      self.CanMaintPredictiveSearch:bool = obj["CanMaintPredictiveSearch"]
      """  CanMaintPredictiveSearch  """  
      self.ThemeID:str = obj["ThemeID"]
      """  ThemeID  """  
      self.DisableTheming:bool = obj["DisableTheming"]
      """  DisableTheming  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanPublishLayout:bool = obj["CanPublishLayout"]
      """  CanPublishLayout  """  
      self.DefaultLayoutID:str = obj["DefaultLayoutID"]
      """  DefaultLayoutID  """  
      self.CanViewDocStar:bool = obj["CanViewDocStar"]
      """  CanViewDocStar  """  
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
      self.AdvancedConfiguratorUser:bool = obj["AdvancedConfiguratorUser"]
      """  flag to indicate Advanced Configurator User  """  
      self.CanOverrideAllocPart:bool = obj["CanOverrideAllocPart"]
      self.ClearPassword:bool = obj["ClearPassword"]
      """  If yes, the user will be able to enter a blank password and still get the prompt for new password.  """  
      self.ExpirePassword:bool = obj["ExpirePassword"]
      """  If yes, the user will be forced to enter his or her current password before he or she will be prompted for the new password.  """  
      self.FailedAttempts:int = obj["FailedAttempts"]
      self.IntegrationAccount:bool = obj["IntegrationAccount"]
      self.LockedOut:bool = obj["LockedOut"]
      self.LockedOutUntil:str = obj["LockedOutUntil"]
      self.PasswordBlank:bool = obj["PasswordBlank"]
      """  set passwrod to blank  """  
      self.PasswordEmail:str = obj["PasswordEmail"]
      """  Email to send new password to  """  
      self.ShpTrackerIntMinute:int = obj["ShpTrackerIntMinute"]
      """  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  """  
      self.UpdateWarning:str = obj["UpdateWarning"]
      """  Update Warning Message  """  
      self.UseCompression:bool = obj["UseCompression"]
      self.AllowReq:bool = obj["AllowReq"]
      """  Whether the user can be referenced as the requestor on a PO Requisition.  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
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
class AccountDisabled_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      pass

class AccountDisabled_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if blank password allowed.  """  
      pass

class AddUserCompany_input:
   """ Required : 
   userID
   data
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user ID for which a company will be added.  """  
      self.data:list[Ice_Tablesets_UserFileTableset] = obj["data"]
      pass

class AddUserCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.data:list[Ice_Tablesets_UserFileTableset] = obj["data"]
      pass

      """  output parameters  """  

class AllowBlankPassword_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if blank password allowed.  """  
      pass

class BackupIdentities_output:
   def __init__(self, obj):
      pass

class BulkUserExportToIdentityProvider_input:
   """ Required : 
   users
   """  
   def __init__(self, obj):
      self.users:str = obj["users"]
      """  List of User ID  """  
      pass

class BulkUserExportToIdentityProvider_output:
   def __init__(self, obj):
      self.returnObj:list[System_Collections_Generic_KeyValuePair_System_String_System_String] = obj["returnObj"]
      """  Dictionary of errors during export. Key - userID, value - error message  """  
      pass

class ChangePassword_input:
   """ Required : 
   userID
   currentPassword
   newPassword
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user identifier.  """  
      self.currentPassword:str = obj["currentPassword"]
      """  The current password.  """  
      self.newPassword:str = obj["newPassword"]
      """  The new password.  """  
      pass

class ChangePassword_output:
   def __init__(self, obj):
      pass

class CheckForCompany_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user identifier.  """  
      pass

class CheckForCompany_output:
   def __init__(self, obj):
      pass

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

class DeleteTemporaryFile_output:
   def __init__(self, obj):
      pass

class DetermineAccessibleInstallationsForUser_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user identifier.  """  
      pass

class DetermineAccessibleInstallationsForUser_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The list of installations that the user has access to.  """  
      pass

class ExpireAllPasswords_input:
   """ Required : 
   blankPasswordsOnly
   disableAccount
   """  
   def __init__(self, obj):
      self.blankPasswordsOnly:bool = obj["blankPasswordsOnly"]
      self.disableAccount:bool = obj["disableAccount"]
      pass

class ExpireAllPasswords_output:
   def __init__(self, obj):
      pass

class ExportUserToIdentityProvider_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  User ID to export  """  
      pass

class ExportUserToIdentityProvider_output:
   def __init__(self, obj):
      pass

class GetAvailableCompanyListForUser_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      pass

class GetAvailableCompanyListForUser_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CompanyListTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_UserFileTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_UserFileTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_UserFileTableset] = obj["returnObj"]
      pass

class GetCompanyListForUser_input:
   """ Required : 
   userID
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  User ID.  """  
      self.whereClause:str = obj["whereClause"]
      """  where clause to apply.  """  
      self.pageSize:int = obj["pageSize"]
      """  page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolute page.  """  
      pass

class GetCompanyListForUser_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CompanyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetCurrentInstallationId_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      pass

class GetCurrentInstallationId_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCurrentUserId_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  User Id record of the logged in user  """  
      pass

class GetExtCompanyList_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Authorized Company  """  
      pass

class GetExtCompanyList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.externalCompanyList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetListCompanyFilter_input:
   """ Required : 
   whereClause
   CompList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.CompList:str = obj["CompList"]
      """  company to filter on  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListCompanyFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UserFileListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Ice_Tablesets_UserFileListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewUserCompExt_input:
   """ Required : 
   ds
   userID
   company
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UserFileTableset] = obj["ds"]
      self.userID:str = obj["userID"]
      self.company:str = obj["company"]
      pass

class GetNewUserCompExt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UserFileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUserComp_input:
   """ Required : 
   ds
   userID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UserFileTableset] = obj["ds"]
      self.userID:str = obj["userID"]
      pass

class GetNewUserComp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UserFileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUserFile_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UserFileTableset] = obj["ds"]
      pass

class GetNewUserFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UserFileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseUserFile
   whereClauseUserComp
   whereClauseUserCompExt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseUserFile:str = obj["whereClauseUserFile"]
      self.whereClauseUserComp:str = obj["whereClauseUserComp"]
      self.whereClauseUserCompExt:str = obj["whereClauseUserCompExt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UserFileTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetUserFile_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UserFileTableset] = obj["returnObj"]
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

class Ice_Tablesets_CompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Name:str = obj["Name"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_CompanyListTableset:
   def __init__(self, obj):
      self.CompanyList:list[Ice_Tablesets_CompanyListRow] = obj["CompanyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtUserFileTableset:
   def __init__(self, obj):
      self.UserFile:list[Ice_Tablesets_UserFileRow] = obj["UserFile"]
      self.UserComp:list[Ice_Tablesets_UserCompRow] = obj["UserComp"]
      self.UserCompExt:list[Ice_Tablesets_UserCompExtRow] = obj["UserCompExt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UserCompExtRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      """  External Company ID  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdateExpense:bool = obj["CanUpdateExpense"]
      """  Indicates if the user can update expense entries (EmpExpense) for any employee.  """  
      self.CanUpdateTime:bool = obj["CanUpdateTime"]
      """  Indicates if the user can update time entries (LaborDtl) for any employee.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.WorkstationID:str = obj["WorkstationID"]
      """  Unique identifier of the Workstations  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanyName:str = obj["CompanyName"]
      self.UserIDName:str = obj["UserIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UserFileListRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.Name:str = obj["Name"]
      """  User Name  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country portion of the address  """  
      self.OfficePhone:str = obj["OfficePhone"]
      """  Office phone number  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  User's email address.  """  
      self.UserDisabled:bool = obj["UserDisabled"]
      """  Indicates if the user account has been disabled (turned off).  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account has security maintenance privileges.  """  
      self.CanChangeSaveSettings:bool = obj["CanChangeSaveSettings"]
      """  Allow user to change save settings  """  
      self.CurComp:str = obj["CurComp"]
      """  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  """  
      self.PwdLastChanged:str = obj["PwdLastChanged"]
      """  Date that the password was last changed.  """  
      self.PwdExpiresDays:int = obj["PwdExpiresDays"]
      """  Password expires x days after the password has been changed.  Zero means the password does not automatically expire.  """  
      self.PwdExpires:str = obj["PwdExpires"]
      """  The date that the user account password expires.  """  
      self.PwdGrace:int = obj["PwdGrace"]
      """  The number of remaining grace logins.  """  
      self.GroupList:str = obj["GroupList"]
      """  List of security groups the user belongs to.  """  
      self.CompList:str = obj["CompList"]
      """  List of companies the user has access to.  """  
      self.ViewFavoriteBar:bool = obj["ViewFavoriteBar"]
      """  Enable Favorite Bar  """  
      self.ViewStatusBar:bool = obj["ViewStatusBar"]
      """  Enable Status Bar  """  
      self.CurFolderSeq:int = obj["CurFolderSeq"]
      """  Sequence number of the folder in focus  """  
      self.CurMenuID:str = obj["CurMenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.DispTips:bool = obj["DispTips"]
      """  Indicates if the user wants tips to be displayed during logon.  """  
      self.CanChangePassword:bool = obj["CanChangePassword"]
      """  Whether the user can change their password.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.LastGraphType:str = obj["LastGraphType"]
      """  The last type of Graph (Bar, 3D Bar, Line, etc.) used in the Schedule Load Graph program.  """  
      self.UseInternalWebBrowser:bool = obj["UseInternalWebBrowser"]
      """  Indicates that the internal web browser should be used instead of using the OS registered browser.  """  
      self.AllowMultipleSessions:bool = obj["AllowMultipleSessions"]
      """  Allow user to start multiple sessions at the same time.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates that the user has Web interface privileges.  When this is turned on, the write trigger maintains certain fields in the WebUser table.  If this is never turned on, a corresponding WebUser doesn't exist.  If this has been on, and is now turned off, the WebUser record is set to disabled, but not deleted.  """  
      self.ListViewMode:int = obj["ListViewMode"]
      """  This property determines the viewing mode of the ListView object. The ListView object supports viewing items in four different modes: Icon(0),SmallIcon(1), List(2) and Report(3). Only 0 1 and 3 are used  """  
      self.CanMaintainFavQueries:bool = obj["CanMaintainFavQueries"]
      """  Whether the user can add/maintain Dashboard Queries on the favorites bar.  """  
      self.CanMaintainFavURLs:bool = obj["CanMaintainFavURLs"]
      """  Whether the user can add/maintain Dashboard URLs on the favorites bar.  """  
      self.CanMaintainFavPrograms:bool = obj["CanMaintainFavPrograms"]
      """  Whether the user can add/maintain Windows Programs on the favorites bar.  """  
      self.CanCustomize:bool = obj["CanCustomize"]
      """  Whether the user can access customization screens.  """  
      self.ViewTreeOnly:int = obj["ViewTreeOnly"]
      """  Whether to display the TreeView alone.  """  
      self.Timeout:int = obj["Timeout"]
      """  Time Out  """  
      self.CanPersonalize:bool = obj["CanPersonalize"]
      """  Whether the user can personalize.  """  
      self.CanTranslate:bool = obj["CanTranslate"]
      """  Whether the user can translate.  """  
      self.CanEditCompAnnotations:bool = obj["CanEditCompAnnotations"]
      """  Can this user edit Company level Help Annotations  """  
      self.CanEditUserAnnotations:bool = obj["CanEditUserAnnotations"]
      """  Can this user edit user level Help Annotations  """  
      self.CanEditHelpLinks:str = obj["CanEditHelpLinks"]
      """  Does this user get access to the HelpLink Editor  """  
      self.AutoStartMonitor:bool = obj["AutoStartMonitor"]
      """  Does this user want the Monitor to Started when they log in. (replaces Config Setting)  """  
      self.MonitorPollingInterval:int = obj["MonitorPollingInterval"]
      """  How frequently (expressed as secounds) the Monitor will poll for results  """  
      self.FormOpenMode:str = obj["FormOpenMode"]
      """  Default form open behavior (Nil, Auto'S'earch, Auto'P'opulate) -  (Replaces Config Setting)  """  
      self.EntConType:str = obj["EntConType"]
      """  Enterprise Connection Type, Determines how the UI Behaves when Session information is changed and UI forms are already present (Nil, 'S'ingleSession, 'M'ultiSession) (Replaces Config Setting)  """  
      self.DashboardDeveloper:bool = obj["DashboardDeveloper"]
      """  Allow user to open dashboards in developer mode  """  
      self.GlbCompSM:bool = obj["GlbCompSM"]
      """   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  """  
      self.LastLogOnAttempt:str = obj["LastLogOnAttempt"]
      """  LastLogOnAttempt  """  
      self.ThemeID:str = obj["ThemeID"]
      """  ThemeID  """  
      self.DisableTheming:bool = obj["DisableTheming"]
      """  DisableTheming  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalIdentity:str = obj["ExternalIdentity"]
      """  ExternalIdentity  """  
      self.SSRSReportDesigner:bool = obj["SSRSReportDesigner"]
      """  SSRSReportDesigner  """  
      self.RestrictIP:bool = obj["RestrictIP"]
      """  RestrictIP  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UserFileListTableset:
   def __init__(self, obj):
      self.UserFileList:list[Ice_Tablesets_UserFileListRow] = obj["UserFileList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UserFileRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.Name:str = obj["Name"]
      """  User Name  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country portion of the address  """  
      self.OfficePhone:str = obj["OfficePhone"]
      """  Office phone number  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  User's email address.  """  
      self.UserDisabled:bool = obj["UserDisabled"]
      """  Indicates if the user account has been disabled (turned off).  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account has security maintenance privileges.  """  
      self.CanChangeSaveSettings:bool = obj["CanChangeSaveSettings"]
      """  Allow user to change save settings  """  
      self.SaveSettings:bool = obj["SaveSettings"]
      """  Save settings  """  
      self.CurComp:str = obj["CurComp"]
      """  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  """  
      self.PwdLastChanged:str = obj["PwdLastChanged"]
      """  Date that the password was last changed.  """  
      self.PwdExpiresDays:int = obj["PwdExpiresDays"]
      """  Password expires x days after the password has been changed.  Zero means the password does not automatically expire.  """  
      self.PwdExpires:str = obj["PwdExpires"]
      """  The date that the user account password expires.  """  
      self.PwdGrace:int = obj["PwdGrace"]
      """  The number of remaining grace logins.  """  
      self.GroupList:str = obj["GroupList"]
      """  List of security groups the user belongs to.  """  
      self.CompList:str = obj["CompList"]
      """  List of companies the user has access to.  """  
      self.ViewFavoriteBar:bool = obj["ViewFavoriteBar"]
      """  Enable Favorite Bar  """  
      self.ViewStatusBar:bool = obj["ViewStatusBar"]
      """  Enable Status Bar  """  
      self.WinX:int = obj["WinX"]
      """  Main menu X-position  """  
      self.WinY:int = obj["WinY"]
      """  Main menu Y-position  """  
      self.CurFolderSeq:int = obj["CurFolderSeq"]
      """  Sequence number of the folder in focus  """  
      self.CurMenuID:str = obj["CurMenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.WinWidth:int = obj["WinWidth"]
      """  Main menu width  """  
      self.WinHeight:int = obj["WinHeight"]
      """  Main menu height  """  
      self.DispTips:bool = obj["DispTips"]
      """  Indicates if the user wants tips to be displayed during logon.  """  
      self.CanChangePassword:bool = obj["CanChangePassword"]
      """  Whether the user can change their password.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.LastGraphType:str = obj["LastGraphType"]
      """  The last type of Graph (Bar, 3D Bar, Line, etc.) used in the Schedule Load Graph program.  """  
      self.UseInternalWebBrowser:bool = obj["UseInternalWebBrowser"]
      """  Indicates that the internal web browser should be used instead of using the OS registered browser.  """  
      self.AllowMultipleSessions:bool = obj["AllowMultipleSessions"]
      """  Allow user to start multiple sessions at the same time.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates that the user has Web interface privileges.  When this is turned on, the write trigger maintains certain fields in the WebUser table.  If this is never turned on, a corresponding WebUser doesn't exist.  If this has been on, and is now turned off, the WebUser record is set to disabled, but not deleted.  """  
      self.ListViewMode:int = obj["ListViewMode"]
      """  This property determines the viewing mode of the ListView object. The ListView object supports viewing items in four different modes: Icon(0),SmallIcon(1), List(2) and Report(3). Only 0 1 and 3 are used  """  
      self.CanMaintainFavQueries:bool = obj["CanMaintainFavQueries"]
      """  Whether the user can add/maintain Dashboard Queries on the favorites bar.  """  
      self.CanMaintainFavURLs:bool = obj["CanMaintainFavURLs"]
      """  Whether the user can add/maintain Dashboard URLs on the favorites bar.  """  
      self.CanMaintainFavPrograms:bool = obj["CanMaintainFavPrograms"]
      """  Whether the user can add/maintain Windows Programs on the favorites bar.  """  
      self.CanCustomize:bool = obj["CanCustomize"]
      """  Whether the user can access customization screens.  """  
      self.ViewTreeOnly:int = obj["ViewTreeOnly"]
      """  Whether to display the TreeView alone.  """  
      self.Timeout:int = obj["Timeout"]
      """  Time Out  """  
      self.CanPersonalize:bool = obj["CanPersonalize"]
      """  Whether the user can personalize.  """  
      self.CanTranslate:bool = obj["CanTranslate"]
      """  Whether the user can translate.  """  
      self.CanEditCompAnnotations:bool = obj["CanEditCompAnnotations"]
      """  Can this user edit Company level Help Annotations  """  
      self.CanEditUserAnnotations:bool = obj["CanEditUserAnnotations"]
      """  Can this user edit user level Help Annotations  """  
      self.CanEditHelpLinks:str = obj["CanEditHelpLinks"]
      """  Does this user get access to the HelpLink Editor  """  
      self.AutoStartMonitor:bool = obj["AutoStartMonitor"]
      """  Does this user want the Monitor to Started when they log in. (replaces Config Setting)  """  
      self.MonitorPollingInterval:int = obj["MonitorPollingInterval"]
      """  How frequently (expressed as secounds) the Monitor will poll for results  """  
      self.FormOpenMode:str = obj["FormOpenMode"]
      """  Default form open behavior (Nil, Auto'S'earch, Auto'P'opulate) -  (Replaces Config Setting)  """  
      self.EntConType:str = obj["EntConType"]
      """  Enterprise Connection Type, Determines how the UI Behaves when Session information is changed and UI forms are already present (Nil, 'S'ingleSession, 'M'ultiSession) (Replaces Config Setting)  """  
      self.DashboardDeveloper:bool = obj["DashboardDeveloper"]
      """  Allow user to open dashboards in developer mode  """  
      self.CanDesignQSearch:bool = obj["CanDesignQSearch"]
      """  Allow user to design quick searches  """  
      self.RequireSso:bool = obj["RequireSso"]
      """   Whether single sign-on (SSO) is required to log on.
Select this check box to indicate that this user has to use his/her operating system (Windows, Unix, and so on) logon information as the logon for Vantage. 
Single Sign-On (SSO) is functionality that allows users to sign on (log in) to Vantage using the Login IDs and Passwords they use to log into their computer's operating system (for example Windows, Unix, Linux and so on). In other words, if SSO is enabled, users will not be presented with a Logon window when they click their Vantage icon; they will be taken directly to the application's main menu.  """  
      self.ViewStatusPanelUserID:bool = obj["ViewStatusPanelUserID"]
      """  Show User ID in status panel  """  
      self.ViewStatusPanelLanguage:bool = obj["ViewStatusPanelLanguage"]
      """  Show language in status panel  """  
      self.ViewStatusPanelCompany:bool = obj["ViewStatusPanelCompany"]
      """  Show current company in status panel  """  
      self.ViewStatusPanelPlant:bool = obj["ViewStatusPanelPlant"]
      """  Show current Site in status panel  """  
      self.ViewStatusPanelServer:bool = obj["ViewStatusPanelServer"]
      """  Show server name in status panel  """  
      self.ViewStatusPanelWorkstationID:bool = obj["ViewStatusPanelWorkstationID"]
      """  Show workstation in status panel  """  
      self.DomainName:str = obj["DomainName"]
      """  Name of the operating system domain into which this users logs in.  Used when Require Single Sign on is enabled.  """  
      self.BPMAdvancedUser:bool = obj["BPMAdvancedUser"]
      """  Determines whether the user is allowed to use advanced development features of Business Process Management.  The freeform editor requires knowledge of Progress 4GL programming and specific method operational working.  Typically freeform options are used by Epicor custom programming or experienced programmers for advanced techniques not available through the wizard-like interface.  """  
      self.MaxGroupsFavorites:int = obj["MaxGroupsFavorites"]
      """  Maximum number of favorite bar groups  """  
      self.MaxGroupsSystemMenu:int = obj["MaxGroupsSystemMenu"]
      """  Maximum number of system menus  """  
      self.OSUserID:str = obj["OSUserID"]
      """  Operating system user ID.  """  
      self.CanTheme:bool = obj["CanTheme"]
      """  Allow user to create themes  """  
      self.FormatCulture:str = obj["FormatCulture"]
      """  Culture format  """  
      self.CanUseEntSearch:bool = obj["CanUseEntSearch"]
      """  yes = the user can use enterprise searches  """  
      self.CanAccEpiEverywhere:bool = obj["CanAccEpiEverywhere"]
      """  Allow access to EWA  """  
      self.CanAcessMobile:bool = obj["CanAcessMobile"]
      """  Allow Acess to Mobile Office  """  
      self.StartMenuClient:str = obj["StartMenuClient"]
      """  Initial start Menu for the Client  """  
      self.StartMenuEWA:str = obj["StartMenuEWA"]
      """  Initial Start Menu ID for EWA  """  
      self.StartMenuMobile:str = obj["StartMenuMobile"]
      """  Initial Start Menu ID for Mobile  """  
      self.AdvBAQRights:bool = obj["AdvBAQRights"]
      """  Allow advanced BAQ designer rights  """  
      self.SecurityAccessOnly:bool = obj["SecurityAccessOnly"]
      """  Defines isthe uesr has Security Access Only  """  
      self.SolutionMgrCreate:bool = obj["SolutionMgrCreate"]
      """  Defines if is user can create a Solution using the Solution Manager  """  
      self.SolutionMgrInstall:bool = obj["SolutionMgrInstall"]
      """  Defines if a user can install Solutions using the Solution Manager  """  
      self.EntSearchURL:str = obj["EntSearchURL"]
      """  Enterprise Search URL  """  
      self.CanMaintQuickSearch:bool = obj["CanMaintQuickSearch"]
      """  Whether the user can add/maintain Quick Searches.  """  
      self.UseDefaultEntSearch:bool = obj["UseDefaultEntSearch"]
      """  Use Default Enterprise Search  """  
      self.UserAccessOnly:bool = obj["UserAccessOnly"]
      """  UserAccessOnly  """  
      self.GlbCompSM:bool = obj["GlbCompSM"]
      """   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  """  
      self.BAQXCompany:bool = obj["BAQXCompany"]
      """  BAQXCompany  """  
      self.LastLogOnAttempt:str = obj["LastLogOnAttempt"]
      """  LastLogOnAttempt  """  
      self.CanImpersonate:bool = obj["CanImpersonate"]
      """  CanImpersonate  """  
      self.ViewStatusPanelSolutionID:bool = obj["ViewStatusPanelSolutionID"]
      """  ViewStatusPanelSolutionID  """  
      self.CanMaintPredictiveSearch:bool = obj["CanMaintPredictiveSearch"]
      """  CanMaintPredictiveSearch  """  
      self.ThemeID:str = obj["ThemeID"]
      """  ThemeID  """  
      self.DisableTheming:bool = obj["DisableTheming"]
      """  DisableTheming  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanPublishLayout:bool = obj["CanPublishLayout"]
      """  CanPublishLayout  """  
      self.DefaultLayoutID:str = obj["DefaultLayoutID"]
      """  DefaultLayoutID  """  
      self.CanViewDocStar:bool = obj["CanViewDocStar"]
      """  CanViewDocStar  """  
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
      self.AdvancedConfiguratorUser:bool = obj["AdvancedConfiguratorUser"]
      """  flag to indicate Advanced Configurator User  """  
      self.CanOverrideAllocPart:bool = obj["CanOverrideAllocPart"]
      self.ClearPassword:bool = obj["ClearPassword"]
      """  If yes, the user will be able to enter a blank password and still get the prompt for new password.  """  
      self.ExpirePassword:bool = obj["ExpirePassword"]
      """  If yes, the user will be forced to enter his or her current password before he or she will be prompted for the new password.  """  
      self.FailedAttempts:int = obj["FailedAttempts"]
      self.IntegrationAccount:bool = obj["IntegrationAccount"]
      self.LockedOut:bool = obj["LockedOut"]
      self.LockedOutUntil:str = obj["LockedOutUntil"]
      self.PasswordBlank:bool = obj["PasswordBlank"]
      """  set passwrod to blank  """  
      self.PasswordEmail:str = obj["PasswordEmail"]
      """  Email to send new password to  """  
      self.ShpTrackerIntMinute:int = obj["ShpTrackerIntMinute"]
      """  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  """  
      self.UpdateWarning:str = obj["UpdateWarning"]
      """  Update Warning Message  """  
      self.UseCompression:bool = obj["UseCompression"]
      self.AllowReq:bool = obj["AllowReq"]
      """  Whether the user can be referenced as the requestor on a PO Requisition.  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
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

class Ice_Tablesets_UserFileTableset:
   def __init__(self, obj):
      self.UserFile:list[Ice_Tablesets_UserFileRow] = obj["UserFile"]
      self.UserComp:list[Ice_Tablesets_UserCompRow] = obj["UserComp"]
      self.UserCompExt:list[Ice_Tablesets_UserCompExtRow] = obj["UserCompExt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class IsPasswordExpired_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user identifier.  """  
      pass

class IsPasswordExpired_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if the password has expired or not set.  """  
      pass

   def parameters(self, obj):
      self.graceCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class IsUserIDAvailable_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      pass

class IsUserIDAvailable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ResetPassword_input:
   """ Required : 
   userID
   setToBlank
   email
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  UserID to change password on.  """  
      self.setToBlank:bool = obj["setToBlank"]
      """  Set to a blank password.  """  
      self.email:str = obj["email"]
      """  Email to send new password to.  """  
      pass

class ResetPassword_output:
   def __init__(self, obj):
      pass

class RestoreIdentities_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The results of the process.  """  
      pass

class SaveSettings_input:
   """ Required : 
   userID
   saveSettings
   currentCompany
   viewFavoriteBar
   viewFullTree
   viewStatusBar
   viewStatusPanelCompany
   viewStatusPanelLanguage
   viewStatusPanelPlant
   viewStatusPanelServer
   viewStatusPanelUserID
   viewStatusPanelWorkstationID
   viewStatusPanelSolutionID
   winX
   winY
   winWidth
   winHeight
   listViewMode
   currentMenuID
   plantID
   workstationID
   currentFolderSequence
   maxGroupsFavorites
   maxGroupsSystemMenu
   themeID
   disableTheming
   defaultFormType
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user identifier.  """  
      self.saveSettings:bool = obj["saveSettings"]
      """  If set to `true` settings are saved.  """  
      self.currentCompany:str = obj["currentCompany"]
      """  The current company.  """  
      self.viewFavoriteBar:bool = obj["viewFavoriteBar"]
      """  If set to `true` then favorite bar is visible.  """  
      self.viewFullTree:bool = obj["viewFullTree"]
      """  If set to `true` then the full tree is visible.  """  
      self.viewStatusBar:bool = obj["viewStatusBar"]
      """  If set to `true` then the status bar is visible.  """  
      self.viewStatusPanelCompany:bool = obj["viewStatusPanelCompany"]
      """  If set to `true` then the status panel company is visible.  """  
      self.viewStatusPanelLanguage:bool = obj["viewStatusPanelLanguage"]
      """  If set to `true` then the status panel language is visible.  """  
      self.viewStatusPanelPlant:bool = obj["viewStatusPanelPlant"]
      """  If set to `true` then the status panel plant is visible.  """  
      self.viewStatusPanelServer:bool = obj["viewStatusPanelServer"]
      """  If set to `true` then the status panel server is visible.  """  
      self.viewStatusPanelUserID:bool = obj["viewStatusPanelUserID"]
      """  If set to `true` then the status panel user identifier is visible.  """  
      self.viewStatusPanelWorkstationID:bool = obj["viewStatusPanelWorkstationID"]
      """  If set to `true` then the status panel workstation identifier is visible.  """  
      self.viewStatusPanelSolutionID:bool = obj["viewStatusPanelSolutionID"]
      """  If set to `true` then the status panel workstation identifier is visible.  """  
      self.winX:int = obj["winX"]
      """  The main window X co-ordinate.  """  
      self.winY:int = obj["winY"]
      """  The main window Y co-ordinate.  """  
      self.winWidth:int = obj["winWidth"]
      """  Width of the main window.  """  
      self.winHeight:int = obj["winHeight"]
      """  Height of the main window.  """  
      self.listViewMode:int = obj["listViewMode"]
      """  The list view mode.  """  
      self.currentMenuID:str = obj["currentMenuID"]
      """  The current menu identifier.  """  
      self.plantID:str = obj["plantID"]
      """  The plant identifier.  """  
      self.workstationID:str = obj["workstationID"]
      """  The workstation identifier.  """  
      self.currentFolderSequence:int = obj["currentFolderSequence"]
      """  The current folder sequence.  """  
      self.maxGroupsFavorites:int = obj["maxGroupsFavorites"]
      """  The max groups favorites.  """  
      self.maxGroupsSystemMenu:int = obj["maxGroupsSystemMenu"]
      """  The max groups system menu.  """  
      self.themeID:str = obj["themeID"]
      """  Theme to be used for this user  """  
      self.disableTheming:bool = obj["disableTheming"]
      """  Disable theming for this user  """  
      self.defaultFormType:str = obj["defaultFormType"]
      """  The default form type the user prefers - WinForm or WebBridge.  """  
      pass

class SaveSettings_output:
   def __init__(self, obj):
      pass

class System_Collections_Generic_KeyValuePair_System_String_System_String:
   def __init__(self, obj):
      self.Key:str = obj["Key"]
      self.Value:str = obj["Value"]
      pass

class UnlockAccount_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      pass

class UnlockAccount_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtUserFileTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtUserFileTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UserFileTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UserFileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePassword_input:
   """ Required : 
   userID
   password
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user identifier.  """  
      self.password:str = obj["password"]
      """  The user's password.  """  
      pass

class ValidatePassword_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if the password is valid.  """  
      pass

