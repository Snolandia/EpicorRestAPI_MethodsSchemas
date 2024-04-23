import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.HelpDeskTopicSvc
# Description: This business object is used to maintain the Topic records (HDTopic)
that are used on Help Desk Cases (HDCase)
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_HelpDeskTopics(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HelpDeskTopics items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HelpDeskTopics
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDTopicRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics",headers=creds) as resp:
           return await resp.json()

async def post_HelpDeskTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HelpDeskTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDTopicRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDTopicRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HelpDeskTopics_Company_TopicID(Company, TopicID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HelpDeskTopic item
   Description: Calls GetByID to retrieve the HelpDeskTopic item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HelpDeskTopic
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDTopicRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics(" + Company + "," + TopicID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HelpDeskTopics_Company_TopicID(Company, TopicID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HelpDeskTopic for the service
   Description: Calls UpdateExt to update HelpDeskTopic. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HelpDeskTopic
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDTopicRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics(" + Company + "," + TopicID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HelpDeskTopics_Company_TopicID(Company, TopicID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HelpDeskTopic item
   Description: Call UpdateExt to delete HelpDeskTopic item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HelpDeskTopic
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics(" + Company + "," + TopicID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDeskTopics_Company_TopicID_HDTopicChilds(Company, TopicID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDTopicChilds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDTopicChilds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDTopicChildRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics(" + Company + "," + TopicID + ")/HDTopicChilds",headers=creds) as resp:
           return await resp.json()

async def get_HelpDeskTopics_Company_TopicID_HDTopicChilds_Company_TopicID_ParentTopicID(Company, TopicID, ParentTopicID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDTopicChild item
   Description: Calls GetByID to retrieve the HDTopicChild item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDTopicChild1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param ParentTopicID: Desc: ParentTopicID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDTopicChildRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics(" + Company + "," + TopicID + ")/HDTopicChilds(" + Company + "," + TopicID + "," + ParentTopicID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDeskTopics_Company_TopicID_HDTopicParents(Company, TopicID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDTopicParents items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDTopicParents1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDTopicParentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics(" + Company + "," + TopicID + ")/HDTopicParents",headers=creds) as resp:
           return await resp.json()

async def get_HelpDeskTopics_Company_TopicID_HDTopicParents_Company_TopicID_ParentTopicID(Company, TopicID, ParentTopicID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDTopicParent item
   Description: Calls GetByID to retrieve the HDTopicParent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDTopicParent1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param ParentTopicID: Desc: ParentTopicID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDTopicParentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HelpDeskTopics(" + Company + "," + TopicID + ")/HDTopicParents(" + Company + "," + TopicID + "," + ParentTopicID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDTopicChilds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDTopicChilds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDTopicChilds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDTopicChildRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicChilds",headers=creds) as resp:
           return await resp.json()

async def post_HDTopicChilds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDTopicChilds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDTopicChildRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDTopicChildRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicChilds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDTopicChilds_Company_TopicID_ParentTopicID(Company, TopicID, ParentTopicID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDTopicChild item
   Description: Calls GetByID to retrieve the HDTopicChild item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDTopicChild
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param ParentTopicID: Desc: ParentTopicID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDTopicChildRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicChilds(" + Company + "," + TopicID + "," + ParentTopicID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDTopicChilds_Company_TopicID_ParentTopicID(Company, TopicID, ParentTopicID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDTopicChild for the service
   Description: Calls UpdateExt to update HDTopicChild. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDTopicChild
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param ParentTopicID: Desc: ParentTopicID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDTopicChildRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicChilds(" + Company + "," + TopicID + "," + ParentTopicID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDTopicChilds_Company_TopicID_ParentTopicID(Company, TopicID, ParentTopicID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDTopicChild item
   Description: Call UpdateExt to delete HDTopicChild item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDTopicChild
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param ParentTopicID: Desc: ParentTopicID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicChilds(" + Company + "," + TopicID + "," + ParentTopicID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDTopicParents(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDTopicParents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDTopicParents
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDTopicParentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicParents",headers=creds) as resp:
           return await resp.json()

async def post_HDTopicParents(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDTopicParents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDTopicParentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDTopicParentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicParents", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDTopicParents_Company_TopicID_ParentTopicID(Company, TopicID, ParentTopicID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDTopicParent item
   Description: Calls GetByID to retrieve the HDTopicParent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDTopicParent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param ParentTopicID: Desc: ParentTopicID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDTopicParentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicParents(" + Company + "," + TopicID + "," + ParentTopicID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDTopicParents_Company_TopicID_ParentTopicID(Company, TopicID, ParentTopicID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDTopicParent for the service
   Description: Calls UpdateExt to update HDTopicParent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDTopicParent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param ParentTopicID: Desc: ParentTopicID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDTopicParentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicParents(" + Company + "," + TopicID + "," + ParentTopicID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDTopicParents_Company_TopicID_ParentTopicID(Company, TopicID, ParentTopicID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDTopicParent item
   Description: Call UpdateExt to delete HDTopicParent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDTopicParent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TopicID: Desc: TopicID   Required: True   Allow empty value : True
      :param ParentTopicID: Desc: ParentTopicID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/HDTopicParents(" + Company + "," + TopicID + "," + ParentTopicID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDTopicListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseHDTopic, whereClauseHDTopicChild, whereClauseHDTopicParent, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseHDTopic=" + whereClauseHDTopic
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDTopicChild=" + whereClauseHDTopicChild
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDTopicParent=" + whereClauseHDTopicParent
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(topicID, epicorHeaders = None):
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
   params += "topicID=" + topicID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTopicParentID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTopicParentID
   Description: Validate that the ParentTopicID isn't a duplicate.
   OperationID: ChangeTopicParentID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTopicParentID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTopicParentID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDTopic(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDTopic
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDTopic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDTopic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDTopic_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDTopicChild(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDTopicChild
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDTopicChild
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDTopicChild_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDTopicChild_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDTopicParent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDTopicParent
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDTopicParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDTopicParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDTopicParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskTopicSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDTopicChildRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDTopicChildRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDTopicListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDTopicListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDTopicParentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDTopicParentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDTopicRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDTopicRow] = obj["value"]
      pass

class Erp_Tablesets_HDTopicChildRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TopicID:str = obj["TopicID"]
      """  A unique identifier for the Help Desk Topic.  """  
      self.ParentTopicID:str = obj["ParentTopicID"]
      """  The TopicID of the parent topic.  """  
      self.ParentSeqNum:int = obj["ParentSeqNum"]
      """   Determines the child topic's sequence within the parent topic.
Any child topics with a duplicate sequence are allowed.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TopicIDDescription:str = obj["TopicIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDTopicListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TopicID:str = obj["TopicID"]
      """  A unique identifier for the Help Desk Topic.  """  
      self.Description:str = obj["Description"]
      """  Full description of the Help Desk topic.  """  
      self.TopLevelTopic:bool = obj["TopLevelTopic"]
      """  If true, this is a topic level topic and can serve as a starting topic in a Help Desk case.  """  
      self.MaintIssue:bool = obj["MaintIssue"]
      """  If topic is available as a Maintenance Issue.  """  
      self.CaseTopic:bool = obj["CaseTopic"]
      """  If this Topic is available in Case Entry  """  
      self.MaintRes:bool = obj["MaintRes"]
      """  If Topic is available as a Maintenance Resolution Topic  """  
      self.GlobalHDTopic:bool = obj["GlobalHDTopic"]
      """  Marks this HDTopic as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDTopicParentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TopicID:str = obj["TopicID"]
      """  A unique identifier for the Help Desk Topic.  """  
      self.ParentTopicID:str = obj["ParentTopicID"]
      """  The TopicID of the parent topic.  """  
      self.ParentSeqNum:int = obj["ParentSeqNum"]
      """   Determines the child topic's sequence within the parent topic.
Any child topics with a duplicate sequence are allowed.  """  
      self.GlobalHDTopicParent:bool = obj["GlobalHDTopicParent"]
      """  Marks this HDTopicParent as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ParentTopicDescription:str = obj["ParentTopicDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDTopicRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TopicID:str = obj["TopicID"]
      """  A unique identifier for the Help Desk Topic.  """  
      self.Description:str = obj["Description"]
      """  Full description of the Help Desk topic.  """  
      self.TopLevelTopic:bool = obj["TopLevelTopic"]
      """  If true, this is a topic level topic and can serve as a starting topic in a Help Desk case.  """  
      self.MaintIssue:bool = obj["MaintIssue"]
      """  If topic is available as a Maintenance Issue.  """  
      self.CaseTopic:bool = obj["CaseTopic"]
      """  If this Topic is available in Case Entry  """  
      self.MaintRes:bool = obj["MaintRes"]
      """  If Topic is available as a Maintenance Resolution Topic  """  
      self.GlobalHDTopic:bool = obj["GlobalHDTopic"]
      """  Marks this HDTopic as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeTopicParentID_input:
   """ Required : 
   ds
   parentTopicID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      self.parentTopicID:str = obj["parentTopicID"]
      """  Parent Topic ID to be validated  """  
      pass

class ChangeTopicParentID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   topicID
   """  
   def __init__(self, obj):
      self.topicID:str = obj["topicID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_HDTopicChildRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TopicID:str = obj["TopicID"]
      """  A unique identifier for the Help Desk Topic.  """  
      self.ParentTopicID:str = obj["ParentTopicID"]
      """  The TopicID of the parent topic.  """  
      self.ParentSeqNum:int = obj["ParentSeqNum"]
      """   Determines the child topic's sequence within the parent topic.
Any child topics with a duplicate sequence are allowed.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TopicIDDescription:str = obj["TopicIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDTopicListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TopicID:str = obj["TopicID"]
      """  A unique identifier for the Help Desk Topic.  """  
      self.Description:str = obj["Description"]
      """  Full description of the Help Desk topic.  """  
      self.TopLevelTopic:bool = obj["TopLevelTopic"]
      """  If true, this is a topic level topic and can serve as a starting topic in a Help Desk case.  """  
      self.MaintIssue:bool = obj["MaintIssue"]
      """  If topic is available as a Maintenance Issue.  """  
      self.CaseTopic:bool = obj["CaseTopic"]
      """  If this Topic is available in Case Entry  """  
      self.MaintRes:bool = obj["MaintRes"]
      """  If Topic is available as a Maintenance Resolution Topic  """  
      self.GlobalHDTopic:bool = obj["GlobalHDTopic"]
      """  Marks this HDTopic as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDTopicListTableset:
   def __init__(self, obj):
      self.HDTopicList:list[Erp_Tablesets_HDTopicListRow] = obj["HDTopicList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_HDTopicParentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TopicID:str = obj["TopicID"]
      """  A unique identifier for the Help Desk Topic.  """  
      self.ParentTopicID:str = obj["ParentTopicID"]
      """  The TopicID of the parent topic.  """  
      self.ParentSeqNum:int = obj["ParentSeqNum"]
      """   Determines the child topic's sequence within the parent topic.
Any child topics with a duplicate sequence are allowed.  """  
      self.GlobalHDTopicParent:bool = obj["GlobalHDTopicParent"]
      """  Marks this HDTopicParent as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ParentTopicDescription:str = obj["ParentTopicDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDTopicRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TopicID:str = obj["TopicID"]
      """  A unique identifier for the Help Desk Topic.  """  
      self.Description:str = obj["Description"]
      """  Full description of the Help Desk topic.  """  
      self.TopLevelTopic:bool = obj["TopLevelTopic"]
      """  If true, this is a topic level topic and can serve as a starting topic in a Help Desk case.  """  
      self.MaintIssue:bool = obj["MaintIssue"]
      """  If topic is available as a Maintenance Issue.  """  
      self.CaseTopic:bool = obj["CaseTopic"]
      """  If this Topic is available in Case Entry  """  
      self.MaintRes:bool = obj["MaintRes"]
      """  If Topic is available as a Maintenance Resolution Topic  """  
      self.GlobalHDTopic:bool = obj["GlobalHDTopic"]
      """  Marks this HDTopic as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HelpDeskTopicTableset:
   def __init__(self, obj):
      self.HDTopic:list[Erp_Tablesets_HDTopicRow] = obj["HDTopic"]
      self.HDTopicChild:list[Erp_Tablesets_HDTopicChildRow] = obj["HDTopicChild"]
      self.HDTopicParent:list[Erp_Tablesets_HDTopicParentRow] = obj["HDTopicParent"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtHelpDeskTopicTableset:
   def __init__(self, obj):
      self.HDTopic:list[Erp_Tablesets_HDTopicRow] = obj["HDTopic"]
      self.HDTopicChild:list[Erp_Tablesets_HDTopicChildRow] = obj["HDTopicChild"]
      self.HDTopicParent:list[Erp_Tablesets_HDTopicParentRow] = obj["HDTopicParent"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   topicID
   """  
   def __init__(self, obj):
      self.topicID:str = obj["topicID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_HDTopicListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewHDTopicChild_input:
   """ Required : 
   ds
   topicID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      self.topicID:str = obj["topicID"]
      pass

class GetNewHDTopicChild_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDTopicParent_input:
   """ Required : 
   ds
   topicID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      self.topicID:str = obj["topicID"]
      pass

class GetNewHDTopicParent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDTopic_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      pass

class GetNewHDTopic_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseHDTopic
   whereClauseHDTopicChild
   whereClauseHDTopicParent
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseHDTopic:str = obj["whereClauseHDTopic"]
      self.whereClauseHDTopicChild:str = obj["whereClauseHDTopicChild"]
      self.whereClauseHDTopicParent:str = obj["whereClauseHDTopicParent"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtHelpDeskTopicTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtHelpDeskTopicTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTopicTableset] = obj["ds"]
      pass

      """  output parameters  """  

