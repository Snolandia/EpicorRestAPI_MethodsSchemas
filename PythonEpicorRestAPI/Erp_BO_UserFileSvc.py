import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.UserFileSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles",headers=creds) as resp:
           return await resp.json()

async def post_UserFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UserFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UserFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UserFiles_DcdUserID(DcdUserID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserFile item
   Description: Calls GetByID to retrieve the UserFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserFile
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UserFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UserFiles_DcdUserID(DcdUserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UserFile for the service
   Description: Calls UpdateExt to update UserFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserFile
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UserFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UserFiles_DcdUserID(DcdUserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UserFile item
   Description: Call UpdateExt to delete UserFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserFile
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_UserFiles_DcdUserID_UserComps(DcdUserID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UserComps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UserComps1
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")/UserComps",headers=creds) as resp:
           return await resp.json()

async def get_UserFiles_DcdUserID_UserComps_DcdUserID_Company(DcdUserID, Company, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserComp item
   Description: Calls GetByID to retrieve the UserComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserComp1
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")/UserComps(" + DcdUserID + "," + Company + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps",headers=creds) as resp:
           return await resp.json()

async def post_UserComps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserComps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UserCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UserCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UserComps_DcdUserID_Company(DcdUserID, Company, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserComp item
   Description: Calls GetByID to retrieve the UserComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserComp
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UserComps_DcdUserID_Company(DcdUserID, Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UserComp for the service
   Description: Calls UpdateExt to update UserComp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserComp
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UserCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UserComps_DcdUserID_Company(DcdUserID, Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UserComp item
   Description: Call UpdateExt to delete UserComp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserComp
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_UserComps_DcdUserID_Company_UserCompExts(DcdUserID, Company, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UserCompExts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UserCompExts1
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompExtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")/UserCompExts",headers=creds) as resp:
           return await resp.json()

async def get_UserComps_DcdUserID_Company_UserCompExts_DcdUserID_Company_ExtCompID(DcdUserID, Company, ExtCompID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserCompExt item
   Description: Calls GetByID to retrieve the UserCompExt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserCompExt1
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompID: Desc: ExtCompID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UserCompExtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")/UserCompExts(" + DcdUserID + "," + Company + "," + ExtCompID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompExtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts",headers=creds) as resp:
           return await resp.json()

async def post_UserCompExts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserCompExts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UserCompExtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UserCompExtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UserCompExts_DcdUserID_Company_ExtCompID(DcdUserID, Company, ExtCompID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserCompExt item
   Description: Calls GetByID to retrieve the UserCompExt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserCompExt
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompID: Desc: ExtCompID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UserCompExtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts(" + DcdUserID + "," + Company + "," + ExtCompID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UserCompExts_DcdUserID_Company_ExtCompID(DcdUserID, Company, ExtCompID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UserCompExt for the service
   Description: Calls UpdateExt to update UserCompExt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserCompExt
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompID: Desc: ExtCompID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UserCompExtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts(" + DcdUserID + "," + Company + "," + ExtCompID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UserCompExts_DcdUserID_Company_ExtCompID(DcdUserID, Company, ExtCompID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UserCompExt item
   Description: Call UpdateExt to delete UserCompExt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserCompExt
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts(" + DcdUserID + "," + Company + "," + ExtCompID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserFileListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(dcdUserID, epicorHeaders = None):
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
   params += "dcdUserID=" + dcdUserID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromList
   Description: Get rows from list dataset
   OperationID: GetRowsFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPayrollRights(epicorHeaders = None):
   """  
   Summary: Invoke method CheckPayrollRights
   Description: Method to call to determine if the user has payroll manager rights
   OperationID: CheckPayrollRights
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPayrollRights_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckAdvancedConfiguratorUser(epicorHeaders = None):
   """  
   Summary: Invoke method CheckAdvancedConfiguratorUser
   Description: Method to call to determine if the user has Advanced Configurator User Rights
   OperationID: CheckAdvancedConfiguratorUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAdvancedConfiguratorUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetUserTimeExpenseRetrieveOptions(epicorHeaders = None):
   """  
   Summary: Invoke method GetUserTimeExpenseRetrieveOptions
   Description: Returns the Time/Expense retrieve options for the current user
   OperationID: GetUserTimeExpenseRetrieveOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserTimeExpenseRetrieveOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SetUserTimeExpenseRetrieveOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUserTimeExpenseRetrieveOptions
   Description: Sets the Time/Expense retrieve options for the current user
   OperationID: SetUserTimeExpenseRetrieveOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUserTimeExpenseRetrieveOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUserTimeExpenseRetrieveOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompExtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UserCompExtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UserCompRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserFileListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UserFileListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserFileRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UserFileRow] = obj["value"]
      pass

class Erp_Tablesets_UserCompExtRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      """  External Company ID  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.PrimBuyerID:str = obj["PrimBuyerID"]
      """  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  """  
      self.OverloadInfHeight:int = obj["OverloadInfHeight"]
      """  Initial height of the Overload Informer in pixels.  """  
      self.OverloadInfSort:str = obj["OverloadInfSort"]
      """  Initial overload informer sort option.  """  
      self.PrimSalesRepID:str = obj["PrimSalesRepID"]
      """  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  """  
      self.StartTaskSaleRepWB:bool = obj["StartTaskSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  """  
      self.StartTaskOppEnt:bool = obj["StartTaskOppEnt"]
      """  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  """  
      self.StartOppSaleRepWB:bool = obj["StartOppSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  """  
      self.StartOrdSaleRepWB:bool = obj["StartOrdSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  """  
      self.StartRMASaleRepWB:bool = obj["StartRMASaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  """  
      self.StartSCallSaleRepWB:bool = obj["StartSCallSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.PrimBuyerID:str = obj["PrimBuyerID"]
      """  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  """  
      self.Name:str = obj["Name"]
      """  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  """  
      self.OverloadInfHeight:int = obj["OverloadInfHeight"]
      """  Initial height of the Overload Informer in pixels.  """  
      self.OverloadInfSort:str = obj["OverloadInfSort"]
      """  Initial overload informer sort option.  """  
      self.PrimSalesRepID:str = obj["PrimSalesRepID"]
      """  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  """  
      self.StartTaskSaleRepWB:bool = obj["StartTaskSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  """  
      self.StartTaskOppEnt:bool = obj["StartTaskOppEnt"]
      """  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  """  
      self.StartOppSaleRepWB:bool = obj["StartOppSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  """  
      self.StartOrdSaleRepWB:bool = obj["StartOrdSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  """  
      self.StartRMASaleRepWB:bool = obj["StartRMASaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  """  
      self.StartSCallSaleRepWB:bool = obj["StartSCallSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  """  
      self.WorkstationID:str = obj["WorkstationID"]
      """  Unique identifier of the Workstations  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.CanUpdateExpense:bool = obj["CanUpdateExpense"]
      """  Indicates if the user can update expense entries (EmpExpense) for any employee.  """  
      self.CanUpdateTime:bool = obj["CanUpdateTime"]
      """  Indicates if the user can update time entries (LaborDtl) for any employee.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FWBLimitedRefresh:bool = obj["FWBLimitedRefresh"]
      """  FWBLimitedRefresh  """  
      self.FWBUseDemandWhseOnly:bool = obj["FWBUseDemandWhseOnly"]
      """  FWBUseDemandWhseOnly  """  
      self.SharedSupValidation:bool = obj["SharedSupValidation"]
      """  Is used by UIApps PurchaseContractScheduleEntry – it is used to set/toggle the Purchase Schedule Approval action menu item Part Schedule Shared Supplier Validation (SharedSupplierValidationToggleTool).  """  
      self.TransactionRetrievalDays:int = obj["TransactionRetrievalDays"]
      """  TransactionRetrievalDays  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanyName:str = obj["CompanyName"]
      self.DCDUserIDName:str = obj["DCDUserIDName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.WorkstationIDDescription:str = obj["WorkstationIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserFileListRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
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
      self.LastDate:str = obj["LastDate"]
      """  Date the user last logged into the system.  """  
      self.LastTime:int = obj["LastTime"]
      """  Time the user last logged into the system.  """  
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
      self.DspPayrollMgr:bool = obj["DspPayrollMgr"]
      """  Payroll Manager field used for display purposes only. See UserFile.PayrollMgr for additional information.  """  
      self.PayrollMgr:str = obj["PayrollMgr"]
      """   Encoded field which indicates if the user is a Payroll Manager.
Only payroll managers can access the Payroll Class and Payroll Manager master files to assign rights to users in regards to viewing or processing payroll information.  """  
      self.ShpTrackerIntMinute:int = obj["ShpTrackerIntMinute"]
      """  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  """  
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
      self.AllowReq:bool = obj["AllowReq"]
      """  Whether the user can be referenced as the requestor on a PO Requisition.  """  
      self.JCDept:str = obj["JCDept"]
      """  Default JC Department for PO Requisitions (ReqDetail.JCDept) created by this user.  This can be left blank or must be valid in the JCDept table.  """  
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
      self.CanSuspend:bool = obj["CanSuspend"]
      """  Whether the user can suspend his session.  """  
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
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspPayrollMgrComp:bool = obj["DspPayrollMgrComp"]
      """  Indicates if the user has payroll manager rights for the current company  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserFileRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
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
      self.LastDate:str = obj["LastDate"]
      """  Date the user last logged into the system.  """  
      self.LastTime:int = obj["LastTime"]
      """  Time the user last logged into the system.  """  
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
      self.DspPayrollMgr:bool = obj["DspPayrollMgr"]
      """  Payroll Manager field used for display purposes only. See UserFile.PayrollMgr for additional information.  """  
      self.PayrollMgr:str = obj["PayrollMgr"]
      """   Encoded field which indicates if the user is a Payroll Manager.
Only payroll managers can access the Payroll Class and Payroll Manager master files to assign rights to users in regards to viewing or processing payroll information.  """  
      self.ShpTrackerIntMinute:int = obj["ShpTrackerIntMinute"]
      """  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  """  
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
      self.AllowReq:bool = obj["AllowReq"]
      """  Whether the user can be referenced as the requestor on a PO Requisition.  """  
      self.JCDept:str = obj["JCDept"]
      """  Default JC Department for PO Requisitions (ReqDetail.JCDept) created by this user.  This can be left blank or must be valid in the JCDept table.  """  
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
      self.CanSuspend:bool = obj["CanSuspend"]
      """  Whether the user can suspend his session.  """  
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
Select this check box to indicate that this user has to use his/her operating system (Windows, Unix, and so on) logon information as the logon for Epicor. 
Single Sign-On (SSO) is functionality that allows users to sign on (log in) to Epicor using the Login IDs and Passwords they use to log into their computer's operating system (for example Windows, Unix, Linux and so on). In other words, if SSO is enabled, users will not be presented with a Logon window when they click their Epicor icon; they will be taken directly to the application main menu.  """  
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
      self.CanOverrideAllocations:bool = obj["CanOverrideAllocations"]
      """  User is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  """  
      self.GlbCompSM:bool = obj["GlbCompSM"]
      """   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  """  
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
      self.TERetrieveApproved:bool = obj["TERetrieveApproved"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  """  
      self.TERetrieveEntered:bool = obj["TERetrieveEntered"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  """  
      self.TERetrieveRejected:bool = obj["TERetrieveRejected"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  """  
      self.TERetrieveSubmitted:bool = obj["TERetrieveSubmitted"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  """  
      self.TERetrievePartiallyApproved:bool = obj["TERetrievePartiallyApproved"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  """  
      self.TEAprRetrieveApproved:bool = obj["TEAprRetrieveApproved"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  """  
      self.TEAprRetrieveEntered:bool = obj["TEAprRetrieveEntered"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  """  
      self.TEAprRetrieveRejected:bool = obj["TEAprRetrieveRejected"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  """  
      self.TEAprRetrieveSubmitted:bool = obj["TEAprRetrieveSubmitted"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  """  
      self.TEAprRetrievePartiallyApproved:bool = obj["TEAprRetrievePartiallyApproved"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  """  
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
      self.MobilePassword:str = obj["MobilePassword"]
      """  MobilePassword  """  
      self.ShopTrackerReuseLast:str = obj["ShopTrackerReuseLast"]
      """  ShopTrackerReuseLast  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdvancedConfiguratorUser:bool = obj["AdvancedConfiguratorUser"]
      """  AdvancedConfiguratorUser  """  
      self.TERetrieveByDay:bool = obj["TERetrieveByDay"]
      """  TERetrieveByDay  """  
      self.TERetrieveByWeek:bool = obj["TERetrieveByWeek"]
      """  TERetrieveByWeek  """  
      self.TERetrieveByMonth:bool = obj["TERetrieveByMonth"]
      """  TERetrieveByMonth  """  
      self.ClearPassword:bool = obj["ClearPassword"]
      """  If yes, the user will be able to enter a blank password and still get the prompt for new password.  """  
      self.DspPayrollMgrComp:bool = obj["DspPayrollMgrComp"]
      """  Indicates if the user has payroll manager rights for the current company  """  
      self.EnableDspPayrollMgr:bool = obj["EnableDspPayrollMgr"]
      """  Indicates if DspPayrollMgr is enabled  """  
      self.EnableDspPayrollMgrComp:bool = obj["EnableDspPayrollMgrComp"]
      """  Indicates if DspPayrollMgrComp is enabled  """  
      self.ExpirePassword:bool = obj["ExpirePassword"]
      """  If yes, the user will be forced to enter his or her current password before he or she will be prompted for the new password.  """  
      self.IsCurCompPayrollMgr:bool = obj["IsCurCompPayrollMgr"]
      self.UseCompression:bool = obj["UseCompression"]
      self.BAQXCompany:bool = obj["BAQXCompany"]
      """  Indicates a user can run BAQ accross multiple companies  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.Character01:str = obj["Character01"]
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.EpicUpgrade_c:bool = obj["EpicUpgrade_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckAdvancedConfiguratorUser_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckPayrollRights_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   dcdUserID
   """  
   def __init__(self, obj):
      self.dcdUserID:str = obj["dcdUserID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtUserFileTableset:
   def __init__(self, obj):
      self.UserFile:list[Erp_Tablesets_UserFileRow] = obj["UserFile"]
      self.UserComp:list[Erp_Tablesets_UserCompRow] = obj["UserComp"]
      self.UserCompExt:list[Erp_Tablesets_UserCompExtRow] = obj["UserCompExt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UserCompExtRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      """  External Company ID  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.PrimBuyerID:str = obj["PrimBuyerID"]
      """  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  """  
      self.OverloadInfHeight:int = obj["OverloadInfHeight"]
      """  Initial height of the Overload Informer in pixels.  """  
      self.OverloadInfSort:str = obj["OverloadInfSort"]
      """  Initial overload informer sort option.  """  
      self.PrimSalesRepID:str = obj["PrimSalesRepID"]
      """  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  """  
      self.StartTaskSaleRepWB:bool = obj["StartTaskSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  """  
      self.StartTaskOppEnt:bool = obj["StartTaskOppEnt"]
      """  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  """  
      self.StartOppSaleRepWB:bool = obj["StartOppSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  """  
      self.StartOrdSaleRepWB:bool = obj["StartOrdSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  """  
      self.StartRMASaleRepWB:bool = obj["StartRMASaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  """  
      self.StartSCallSaleRepWB:bool = obj["StartSCallSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.PrimBuyerID:str = obj["PrimBuyerID"]
      """  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  """  
      self.Name:str = obj["Name"]
      """  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  """  
      self.OverloadInfHeight:int = obj["OverloadInfHeight"]
      """  Initial height of the Overload Informer in pixels.  """  
      self.OverloadInfSort:str = obj["OverloadInfSort"]
      """  Initial overload informer sort option.  """  
      self.PrimSalesRepID:str = obj["PrimSalesRepID"]
      """  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  """  
      self.StartTaskSaleRepWB:bool = obj["StartTaskSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  """  
      self.StartTaskOppEnt:bool = obj["StartTaskOppEnt"]
      """  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  """  
      self.StartOppSaleRepWB:bool = obj["StartOppSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  """  
      self.StartOrdSaleRepWB:bool = obj["StartOrdSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  """  
      self.StartRMASaleRepWB:bool = obj["StartRMASaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  """  
      self.StartSCallSaleRepWB:bool = obj["StartSCallSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  """  
      self.WorkstationID:str = obj["WorkstationID"]
      """  Unique identifier of the Workstations  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.CanUpdateExpense:bool = obj["CanUpdateExpense"]
      """  Indicates if the user can update expense entries (EmpExpense) for any employee.  """  
      self.CanUpdateTime:bool = obj["CanUpdateTime"]
      """  Indicates if the user can update time entries (LaborDtl) for any employee.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FWBLimitedRefresh:bool = obj["FWBLimitedRefresh"]
      """  FWBLimitedRefresh  """  
      self.FWBUseDemandWhseOnly:bool = obj["FWBUseDemandWhseOnly"]
      """  FWBUseDemandWhseOnly  """  
      self.SharedSupValidation:bool = obj["SharedSupValidation"]
      """  Is used by UIApps PurchaseContractScheduleEntry – it is used to set/toggle the Purchase Schedule Approval action menu item Part Schedule Shared Supplier Validation (SharedSupplierValidationToggleTool).  """  
      self.TransactionRetrievalDays:int = obj["TransactionRetrievalDays"]
      """  TransactionRetrievalDays  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanyName:str = obj["CompanyName"]
      self.DCDUserIDName:str = obj["DCDUserIDName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.WorkstationIDDescription:str = obj["WorkstationIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserFileListRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
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
      self.LastDate:str = obj["LastDate"]
      """  Date the user last logged into the system.  """  
      self.LastTime:int = obj["LastTime"]
      """  Time the user last logged into the system.  """  
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
      self.DspPayrollMgr:bool = obj["DspPayrollMgr"]
      """  Payroll Manager field used for display purposes only. See UserFile.PayrollMgr for additional information.  """  
      self.PayrollMgr:str = obj["PayrollMgr"]
      """   Encoded field which indicates if the user is a Payroll Manager.
Only payroll managers can access the Payroll Class and Payroll Manager master files to assign rights to users in regards to viewing or processing payroll information.  """  
      self.ShpTrackerIntMinute:int = obj["ShpTrackerIntMinute"]
      """  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  """  
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
      self.AllowReq:bool = obj["AllowReq"]
      """  Whether the user can be referenced as the requestor on a PO Requisition.  """  
      self.JCDept:str = obj["JCDept"]
      """  Default JC Department for PO Requisitions (ReqDetail.JCDept) created by this user.  This can be left blank or must be valid in the JCDept table.  """  
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
      self.CanSuspend:bool = obj["CanSuspend"]
      """  Whether the user can suspend his session.  """  
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
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspPayrollMgrComp:bool = obj["DspPayrollMgrComp"]
      """  Indicates if the user has payroll manager rights for the current company  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserFileListTableset:
   def __init__(self, obj):
      self.UserFileList:list[Erp_Tablesets_UserFileListRow] = obj["UserFileList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UserFileRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
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
      self.LastDate:str = obj["LastDate"]
      """  Date the user last logged into the system.  """  
      self.LastTime:int = obj["LastTime"]
      """  Time the user last logged into the system.  """  
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
      self.DspPayrollMgr:bool = obj["DspPayrollMgr"]
      """  Payroll Manager field used for display purposes only. See UserFile.PayrollMgr for additional information.  """  
      self.PayrollMgr:str = obj["PayrollMgr"]
      """   Encoded field which indicates if the user is a Payroll Manager.
Only payroll managers can access the Payroll Class and Payroll Manager master files to assign rights to users in regards to viewing or processing payroll information.  """  
      self.ShpTrackerIntMinute:int = obj["ShpTrackerIntMinute"]
      """  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  """  
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
      self.AllowReq:bool = obj["AllowReq"]
      """  Whether the user can be referenced as the requestor on a PO Requisition.  """  
      self.JCDept:str = obj["JCDept"]
      """  Default JC Department for PO Requisitions (ReqDetail.JCDept) created by this user.  This can be left blank or must be valid in the JCDept table.  """  
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
      self.CanSuspend:bool = obj["CanSuspend"]
      """  Whether the user can suspend his session.  """  
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
Select this check box to indicate that this user has to use his/her operating system (Windows, Unix, and so on) logon information as the logon for Epicor. 
Single Sign-On (SSO) is functionality that allows users to sign on (log in) to Epicor using the Login IDs and Passwords they use to log into their computer's operating system (for example Windows, Unix, Linux and so on). In other words, if SSO is enabled, users will not be presented with a Logon window when they click their Epicor icon; they will be taken directly to the application main menu.  """  
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
      self.CanOverrideAllocations:bool = obj["CanOverrideAllocations"]
      """  User is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  """  
      self.GlbCompSM:bool = obj["GlbCompSM"]
      """   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  """  
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
      self.TERetrieveApproved:bool = obj["TERetrieveApproved"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  """  
      self.TERetrieveEntered:bool = obj["TERetrieveEntered"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  """  
      self.TERetrieveRejected:bool = obj["TERetrieveRejected"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  """  
      self.TERetrieveSubmitted:bool = obj["TERetrieveSubmitted"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  """  
      self.TERetrievePartiallyApproved:bool = obj["TERetrievePartiallyApproved"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  """  
      self.TEAprRetrieveApproved:bool = obj["TEAprRetrieveApproved"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  """  
      self.TEAprRetrieveEntered:bool = obj["TEAprRetrieveEntered"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  """  
      self.TEAprRetrieveRejected:bool = obj["TEAprRetrieveRejected"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  """  
      self.TEAprRetrieveSubmitted:bool = obj["TEAprRetrieveSubmitted"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  """  
      self.TEAprRetrievePartiallyApproved:bool = obj["TEAprRetrievePartiallyApproved"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  """  
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
      self.MobilePassword:str = obj["MobilePassword"]
      """  MobilePassword  """  
      self.ShopTrackerReuseLast:str = obj["ShopTrackerReuseLast"]
      """  ShopTrackerReuseLast  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdvancedConfiguratorUser:bool = obj["AdvancedConfiguratorUser"]
      """  AdvancedConfiguratorUser  """  
      self.TERetrieveByDay:bool = obj["TERetrieveByDay"]
      """  TERetrieveByDay  """  
      self.TERetrieveByWeek:bool = obj["TERetrieveByWeek"]
      """  TERetrieveByWeek  """  
      self.TERetrieveByMonth:bool = obj["TERetrieveByMonth"]
      """  TERetrieveByMonth  """  
      self.ClearPassword:bool = obj["ClearPassword"]
      """  If yes, the user will be able to enter a blank password and still get the prompt for new password.  """  
      self.DspPayrollMgrComp:bool = obj["DspPayrollMgrComp"]
      """  Indicates if the user has payroll manager rights for the current company  """  
      self.EnableDspPayrollMgr:bool = obj["EnableDspPayrollMgr"]
      """  Indicates if DspPayrollMgr is enabled  """  
      self.EnableDspPayrollMgrComp:bool = obj["EnableDspPayrollMgrComp"]
      """  Indicates if DspPayrollMgrComp is enabled  """  
      self.ExpirePassword:bool = obj["ExpirePassword"]
      """  If yes, the user will be forced to enter his or her current password before he or she will be prompted for the new password.  """  
      self.IsCurCompPayrollMgr:bool = obj["IsCurCompPayrollMgr"]
      self.UseCompression:bool = obj["UseCompression"]
      self.BAQXCompany:bool = obj["BAQXCompany"]
      """  Indicates a user can run BAQ accross multiple companies  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.Character01:str = obj["Character01"]
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.EpicUpgrade_c:bool = obj["EpicUpgrade_c"]
      pass

class Erp_Tablesets_UserFileTableset:
   def __init__(self, obj):
      self.UserFile:list[Erp_Tablesets_UserFileRow] = obj["UserFile"]
      self.UserComp:list[Erp_Tablesets_UserCompRow] = obj["UserComp"]
      self.UserCompExt:list[Erp_Tablesets_UserCompExtRow] = obj["UserCompExt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   dcdUserID
   """  
   def __init__(self, obj):
      self.dcdUserID:str = obj["dcdUserID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_UserFileTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UserFileTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UserFileTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UserFileListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewUserCompExt_input:
   """ Required : 
   ds
   dcdUserID
   company
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UserFileTableset] = obj["ds"]
      self.dcdUserID:str = obj["dcdUserID"]
      self.company:str = obj["company"]
      pass

class GetNewUserCompExt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UserFileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUserComp_input:
   """ Required : 
   ds
   dcdUserID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UserFileTableset] = obj["ds"]
      self.dcdUserID:str = obj["dcdUserID"]
      pass

class GetNewUserComp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UserFileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUserFile_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UserFileTableset] = obj["ds"]
      pass

class GetNewUserFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UserFileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsFromList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UserFileListTableset] = obj["ds"]
      pass

class GetRowsFromList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_UserFileTableset] = obj["returnObj"]
      pass

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
      self.returnObj:list[Erp_Tablesets_UserFileTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetUserTimeExpenseRetrieveOptions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.retrieveApproved:bool = obj["retrieveApproved"]
      self.retrieveEntered:bool = obj["retrieveEntered"]
      self.retrievePartiallyApproved:bool = obj["retrievePartiallyApproved"]
      self.retrieveRejected:bool = obj["retrieveRejected"]
      self.retrieveSubmitted:bool = obj["retrieveSubmitted"]
      self.retrieveByDay:bool = obj["retrieveByDay"]
      self.retrieveByMonth:bool = obj["retrieveByMonth"]
      self.retrieveByWeek:bool = obj["retrieveByWeek"]
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

class SetUserTimeExpenseRetrieveOptions_input:
   """ Required : 
   retrieveApproved
   retrieveEntered
   retrievePartiallyApproved
   retrieveRejected
   retrieveSubmitted
   retrieveByDay
   retrieveByMonth
   retrieveByWeek
   """  
   def __init__(self, obj):
      self.retrieveApproved:bool = obj["retrieveApproved"]
      """  Retrieve approved  """  
      self.retrieveEntered:bool = obj["retrieveEntered"]
      """  Retrieve entered  """  
      self.retrievePartiallyApproved:bool = obj["retrievePartiallyApproved"]
      """  Retrieve partially approved  """  
      self.retrieveRejected:bool = obj["retrieveRejected"]
      """  Retrieve rejected  """  
      self.retrieveSubmitted:bool = obj["retrieveSubmitted"]
      """  Retrieve submitted  """  
      self.retrieveByDay:bool = obj["retrieveByDay"]
      """  Retrieve by date  """  
      self.retrieveByMonth:bool = obj["retrieveByMonth"]
      """  Retrieve by month  """  
      self.retrieveByWeek:bool = obj["retrieveByWeek"]
      """  Retrieve by week  """  
      pass

class SetUserTimeExpenseRetrieveOptions_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUserFileTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUserFileTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UserFileTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UserFileTableset] = obj["ds"]
      pass

      """  output parameters  """  

