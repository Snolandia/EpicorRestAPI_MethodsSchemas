import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.StructuredOutputDefinitionSvc
# Description: BO for the Structured Output Definition UI.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_StructuredOutputDefinitions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get StructuredOutputDefinitions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_StructuredOutputDefinitions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions",headers=creds) as resp:
           return await resp.json()

async def post_StructuredOutputDefinitions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_StructuredOutputDefinitions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_StructuredOutputDefinitions_RptStructuredOutputDefID(RptStructuredOutputDefID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the StructuredOutputDefinition item
   Description: Calls GetByID to retrieve the StructuredOutputDefinition item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_StructuredOutputDefinition
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_StructuredOutputDefinitions_RptStructuredOutputDefID(RptStructuredOutputDefID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update StructuredOutputDefinition for the service
   Description: Calls UpdateExt to update StructuredOutputDefinition. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_StructuredOutputDefinition
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_StructuredOutputDefinitions_RptStructuredOutputDefID(RptStructuredOutputDefID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete StructuredOutputDefinition item
   Description: Call UpdateExt to delete StructuredOutputDefinition item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_StructuredOutputDefinition
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")",headers=creds) as resp:
           return await resp.json()

async def get_StructuredOutputDefinitions_RptStructuredOutputDefID_RptStructuredOutputFiles(RptStructuredOutputDefID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptStructuredOutputFiles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptStructuredOutputFiles1
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")/RptStructuredOutputFiles",headers=creds) as resp:
           return await resp.json()

async def get_StructuredOutputDefinitions_RptStructuredOutputDefID_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID(RptStructuredOutputDefID, RptStructuredOutputFileID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFile item
   Description: Calls GetByID to retrieve the RptStructuredOutputFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFile1
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFiles(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptStructuredOutputFiles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptStructuredOutputFiles
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles",headers=creds) as resp:
           return await resp.json()

async def post_RptStructuredOutputFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptStructuredOutputFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID(RptStructuredOutputDefID, RptStructuredOutputFileID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFile item
   Description: Calls GetByID to retrieve the RptStructuredOutputFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFile
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID(RptStructuredOutputDefID, RptStructuredOutputFileID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptStructuredOutputFile for the service
   Description: Calls UpdateExt to update RptStructuredOutputFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptStructuredOutputFile
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID(RptStructuredOutputDefID, RptStructuredOutputFileID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptStructuredOutputFile item
   Description: Call UpdateExt to delete RptStructuredOutputFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptStructuredOutputFile
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileElements(RptStructuredOutputDefID, RptStructuredOutputFileID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptStructuredOutputFileElements items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptStructuredOutputFileElements1
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileElementRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")/RptStructuredOutputFileElements",headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileElements_RptStructuredOutputDefID_RptStructuredOutputFileID_ElementID(RptStructuredOutputDefID, RptStructuredOutputFileID, ElementID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFileElement item
   Description: Calls GetByID to retrieve the RptStructuredOutputFileElement item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFileElement1
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param ElementID: Desc: ElementID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")/RptStructuredOutputFileElements(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + ElementID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileXMLNS(RptStructuredOutputDefID, RptStructuredOutputFileID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptStructuredOutputFileXMLNS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptStructuredOutputFileXMLNS1
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")/RptStructuredOutputFileXMLNS",headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileXMLNS_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileNamespaceID(RptStructuredOutputDefID, RptStructuredOutputFileID, RptStructuredOutputFileNamespaceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFileXMLN item
   Description: Calls GetByID to retrieve the RptStructuredOutputFileXMLN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFileXMLN1
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileNamespaceID: Desc: RptStructuredOutputFileNamespaceID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")/RptStructuredOutputFileXMLNS(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + RptStructuredOutputFileNamespaceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFileElements(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptStructuredOutputFileElements items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptStructuredOutputFileElements
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileElementRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements",headers=creds) as resp:
           return await resp.json()

async def post_RptStructuredOutputFileElements(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptStructuredOutputFileElements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFileElements_RptStructuredOutputDefID_RptStructuredOutputFileID_ElementID(RptStructuredOutputDefID, RptStructuredOutputFileID, ElementID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFileElement item
   Description: Calls GetByID to retrieve the RptStructuredOutputFileElement item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFileElement
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param ElementID: Desc: ElementID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + ElementID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptStructuredOutputFileElements_RptStructuredOutputDefID_RptStructuredOutputFileID_ElementID(RptStructuredOutputDefID, RptStructuredOutputFileID, ElementID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptStructuredOutputFileElement for the service
   Description: Calls UpdateExt to update RptStructuredOutputFileElement. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptStructuredOutputFileElement
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param ElementID: Desc: ElementID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + ElementID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptStructuredOutputFileElements_RptStructuredOutputDefID_RptStructuredOutputFileID_ElementID(RptStructuredOutputDefID, RptStructuredOutputFileID, ElementID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptStructuredOutputFileElement item
   Description: Call UpdateExt to delete RptStructuredOutputFileElement item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptStructuredOutputFileElement
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param ElementID: Desc: ElementID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + ElementID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFileXMLNS(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptStructuredOutputFileXMLNS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptStructuredOutputFileXMLNS
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS",headers=creds) as resp:
           return await resp.json()

async def post_RptStructuredOutputFileXMLNS(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptStructuredOutputFileXMLNS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptStructuredOutputFileXMLNS_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileNamespaceID(RptStructuredOutputDefID, RptStructuredOutputFileID, RptStructuredOutputFileNamespaceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFileXMLN item
   Description: Calls GetByID to retrieve the RptStructuredOutputFileXMLN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFileXMLN
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileNamespaceID: Desc: RptStructuredOutputFileNamespaceID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + RptStructuredOutputFileNamespaceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptStructuredOutputFileXMLNS_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileNamespaceID(RptStructuredOutputDefID, RptStructuredOutputFileID, RptStructuredOutputFileNamespaceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptStructuredOutputFileXMLN for the service
   Description: Calls UpdateExt to update RptStructuredOutputFileXMLN. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptStructuredOutputFileXMLN
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileNamespaceID: Desc: RptStructuredOutputFileNamespaceID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + RptStructuredOutputFileNamespaceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptStructuredOutputFileXMLNS_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileNamespaceID(RptStructuredOutputDefID, RptStructuredOutputFileID, RptStructuredOutputFileNamespaceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptStructuredOutputFileXMLN item
   Description: Call UpdateExt to delete RptStructuredOutputFileXMLN item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptStructuredOutputFileXMLN
      :param RptStructuredOutputDefID: Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileID: Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      :param RptStructuredOutputFileNamespaceID: Desc: RptStructuredOutputFileNamespaceID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + RptStructuredOutputFileNamespaceID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRptStructuredOutputDef, whereClauseRptStructuredOutputFile, whereClauseRptStructuredOutputFileElement, whereClauseRptStructuredOutputFileXMLNS, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseRptStructuredOutputDef=" + whereClauseRptStructuredOutputDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptStructuredOutputFile=" + whereClauseRptStructuredOutputFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptStructuredOutputFileElement=" + whereClauseRptStructuredOutputFileElement
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptStructuredOutputFileXMLNS=" + whereClauseRptStructuredOutputFileXMLNS
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rptStructuredOutputDefID, epicorHeaders = None):
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
   params += "rptStructuredOutputDefID=" + rptStructuredOutputDefID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeReportDataDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeReportDataDefinition
   Description: Called when user changes the report data definition for the structured output definition.
   OperationID: OnChangeReportDataDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeReportDataDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReportDataDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAllOutputFileElements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAllOutputFileElements
   Description: Deletes all output file elements.
   OperationID: DeleteAllOutputFileElements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAllOutputFileElements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAllOutputFileElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOutputLocation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOutputLocation
   Description: Called when user changes the output location for the structured output file.
   OperationID: OnChangeOutputLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOutputLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOutputLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataSourceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataSourceList
   Description: Get data source list (for data source combo box). Column table will be empty.
   OperationID: GetDataSourceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataSourceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataSourceColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataSourceColumns
   Description: Get columns for data source (for data column combo box). Data source table will be empty.
   OperationID: GetDataSourceColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataSourceColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataSourceListWithIsUsedSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataSourceListWithIsUsedSet
   Description: Get data source list with IsUsed set
   OperationID: GetDataSourceListWithIsUsedSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataSourceListWithIsUsedSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceListWithIsUsedSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataSourceColumnType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataSourceColumnType
   Description: Get data source column data type.
   OperationID: GetDataSourceColumnType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataSourceColumnType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceColumnType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOutputFileElements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOutputFileElements
   Description: Validate structured output file elements.
   OperationID: ValidateOutputFileElements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOutputFileElements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOutputFileElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOutputFileElement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOutputFileElement
   Description: Validate structured output file element.
   OperationID: ValidateOutputFileElement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOutputFileElement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOutputFileElement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportFile
   Description: Imports file with XML data or json schema.
   OperationID: ImportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportJSONSchema(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportJSONSchema
   Description: Imports the json schema.
   OperationID: ImportJSONSchema
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportJSONSchema_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportJSONSchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateStructuredOutputDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateStructuredOutputDef
   Description: Duplicates a Structured Output Definition
   OperationID: DuplicateStructuredOutputDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateStructuredOutputDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateStructuredOutputDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateStructuredOutputFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateStructuredOutputFile
   Description: Duplicates a Structured Output File
   OperationID: DuplicateStructuredOutputFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateStructuredOutputFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateStructuredOutputFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportXmlDataWithValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportXmlDataWithValues
   Description: Imports the XML data.
   OperationID: ImportXmlDataWithValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportXmlDataWithValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportXmlDataWithValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportXmlDataWithNoValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportXmlDataWithNoValues
   Description: Imports the XML data.
   OperationID: ImportXmlDataWithNoValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportXmlDataWithNoValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportXmlDataWithNoValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEICalculators(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEICalculators
   Description: Get Electronic Interface Calculator Names in tilde-separated string (for calculation name combo box)
   OperationID: GetEICalculators
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEICalculators_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEICalculators_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAncestorDataSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAncestorDataSource
   Description: Get the DataSource value from the most immediate ancestor of the file element
   OperationID: GetAncestorDataSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAncestorDataSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAncestorDataSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DescendantsWithDataSourceIdExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DescendantsWithDataSourceIdExist
   Description: Check if descendants with DataSourceId = original DataSourceId value exist
   OperationID: DescendantsWithDataSourceIdExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DescendantsWithDataSourceIdExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DescendantsWithDataSourceIdExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDescendantsWithNewDataSourceId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDescendantsWithNewDataSourceId
   Description: Update descendants having DataSourceId = original DataSourceId value with new DataSourceID value
   OperationID: UpdateDescendantsWithNewDataSourceId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDescendantsWithNewDataSourceId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDescendantsWithNewDataSourceId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptStructuredOutputDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptStructuredOutputDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStructuredOutputDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptStructuredOutputDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStructuredOutputDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptStructuredOutputFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptStructuredOutputFile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStructuredOutputFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptStructuredOutputFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStructuredOutputFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptStructuredOutputFileElement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptStructuredOutputFileElement
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStructuredOutputFileElement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptStructuredOutputFileElement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStructuredOutputFileElement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptStructuredOutputFileXMLNS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptStructuredOutputFileXMLNS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStructuredOutputFileXMLNS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptStructuredOutputFileXMLNS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStructuredOutputFileXMLNS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptStructuredOutputDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptStructuredOutputDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileElementRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptStructuredOutputFileElementRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptStructuredOutputFileRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileXMLNSRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptStructuredOutputFileXMLNSRow] = obj["value"]
      pass

class Ice_Tablesets_RptStructuredOutputDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputDescription:str = obj["RptStructuredOutputDescription"]
      """  RptStructuredOutputDescription  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.ConfirmedCompliance:bool = obj["ConfirmedCompliance"]
      """  ConfirmedCompliance  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RptDataDefRptDescription:str = obj["RptDataDefRptDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStructuredOutputDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputDescription:str = obj["RptStructuredOutputDescription"]
      """  RptStructuredOutputDescription  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.ConfirmedCompliance:bool = obj["ConfirmedCompliance"]
      """  ConfirmedCompliance  """  
      self.ComplianceRule:str = obj["ComplianceRule"]
      """  ComplianceRule  """  
      self.InternalComments:str = obj["InternalComments"]
      """  InternalComments  """  
      self.DateFormat:str = obj["DateFormat"]
      """  DateFormat  """  
      self.DecimalSymbol:str = obj["DecimalSymbol"]
      """  DecimalSymbol  """  
      self.DigitGroupingSymbol:str = obj["DigitGroupingSymbol"]
      """  DigitGroupingSymbol  """  
      self.NegativeSignSymbol:str = obj["NegativeSignSymbol"]
      """  NegativeSignSymbol  """  
      self.Encoding:str = obj["Encoding"]
      """  Encoding  """  
      self.Delimiter:str = obj["Delimiter"]
      """  Delimiter  """  
      self.EndOfRecordSymbol:str = obj["EndOfRecordSymbol"]
      """  EndOfRecordSymbol  """  
      self.QuotationMark:str = obj["QuotationMark"]
      """  QuotationMark  """  
      self.QuoteAllValues:bool = obj["QuoteAllValues"]
      """  QuoteAllValues  """  
      self.BooleanTrue:str = obj["BooleanTrue"]
      """  BooleanTrue  """  
      self.BooleanFalse:str = obj["BooleanFalse"]
      """  BooleanFalse  """  
      self.PrePostProcessingEFTHeadCompany:str = obj["PrePostProcessingEFTHeadCompany"]
      """  PrePostProcessingEFTHeadCompany  """  
      self.PrePostProcessingEFTHeadUID:int = obj["PrePostProcessingEFTHeadUID"]
      """  PrePostProcessingEFTHeadUID  """  
      self.AdditionalSettings:str = obj["AdditionalSettings"]
      """  AdditionalSettings  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PrePostProcessingDescription:str = obj["PrePostProcessingDescription"]
      """  Description for the PrePostProcessingEFTHeadUID  """  
      self.PrePostProcessingName:str = obj["PrePostProcessingName"]
      """  Name of the PrePostProcessingEFTHeadUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RptDataDefSystemRpt:bool = obj["RptDataDefSystemRpt"]
      self.RptDataDefRptDescription:str = obj["RptDataDefRptDescription"]
      self.RptDataDefDuplicateOf:str = obj["RptDataDefDuplicateOf"]
      self.RptDataDefRptTypeID:str = obj["RptDataDefRptTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStructuredOutputFileElementRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputFileID:str = obj["RptStructuredOutputFileID"]
      """  RptStructuredOutputFileID  """  
      self.ElementID:int = obj["ElementID"]
      """  ElementID  """  
      self.ElementName:str = obj["ElementName"]
      """  ElementName  """  
      self.ParentElementID:int = obj["ParentElementID"]
      """  ParentElementID  """  
      self.ChildSequence:int = obj["ChildSequence"]
      """  ChildSequence  """  
      self.Namespace:str = obj["Namespace"]
      """  Namespace  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.XMLAttribute:bool = obj["XMLAttribute"]
      """  XMLAttribute  """  
      self.AggregationType:int = obj["AggregationType"]
      """  AggregationType  """  
      self.DecimalScale:int = obj["DecimalScale"]
      """  DecimalScale  """  
      self.DataSourceID:str = obj["DataSourceID"]
      """  DataSourceID  """  
      self.DataSourceColumn:str = obj["DataSourceColumn"]
      """  DataSourceColumn  """  
      self.IsConstant:bool = obj["IsConstant"]
      """  IsConstant  """  
      self.ConstantValue:str = obj["ConstantValue"]
      """  ConstantValue  """  
      self.CalculationEFTHeadCompany:str = obj["CalculationEFTHeadCompany"]
      """  CalculationEFTHeadCompany  """  
      self.CalculationEFTHeadUID:int = obj["CalculationEFTHeadUID"]
      """  CalculationEFTHeadUID  """  
      self.CalculationName:str = obj["CalculationName"]
      """  CalculationName  """  
      self.AdditionalSettings:str = obj["AdditionalSettings"]
      """  AdditionalSettings  """  
      self.DateFormat:str = obj["DateFormat"]
      """  DateFormat  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.JSONObject:bool = obj["JSONObject"]
      """  JSONObject  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ElementDataType:str = obj["ElementDataType"]
      """  ElementDataType  """  
      self.ElementDescription:str = obj["ElementDescription"]
      """  ElementDescription  """  
      self.EmptyStringGenerateEmptyElement:bool = obj["EmptyStringGenerateEmptyElement"]
      """  EmptyStringGenerateEmptyElement  """  
      self.EmptyStringSuppressOrNullElement:bool = obj["EmptyStringSuppressOrNullElement"]
      """  EmptyStringSuppressOrNullElement  """  
      self.EmptyStringSubsituteElement:bool = obj["EmptyStringSubsituteElement"]
      """  EmptyStringSubsituteElement  """  
      self.EmptyStringSubsituteValue:str = obj["EmptyStringSubsituteValue"]
      """  EmptyStringSubsituteValue  """  
      self.ZeroNumericSuppress:bool = obj["ZeroNumericSuppress"]
      """  ZeroNumericSuppress  """  
      self.NeedSign:bool = obj["NeedSign"]
      """  NeedSign  """  
      self.CalculationEFTHeadName:str = obj["CalculationEFTHeadName"]
      """  CalculationEFTHeadName  """  
      self.DataSourceColumnDataType:str = obj["DataSourceColumnDataType"]
      """  .NET Data type for the datasource column.  """  
      self.ElementFullName:str = obj["ElementFullName"]
      """  Element name including the prefix. Prefix:ElementName or ElementName if Prefix=""  """  
      self.ValidationErrorColumns:str = obj["ValidationErrorColumns"]
      """  List of table columns with validation rules.  """  
      self.ValidationMessage:str = obj["ValidationMessage"]
      """  Validation message from all columns.  """  
      self.IsDocLevelPrefix:bool = obj["IsDocLevelPrefix"]
      """  Is Doc Level Prefix  """  
      self.DocLevelNamespace:str = obj["DocLevelNamespace"]
      """  Doc Level Namespace  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStructuredOutputFileRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputFileID:str = obj["RptStructuredOutputFileID"]
      """  RptStructuredOutputFileID  """  
      self.RptStructuredOutputFileDesc:str = obj["RptStructuredOutputFileDesc"]
      """  RptStructuredOutputFileDesc  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled  """  
      self.StructuredOutputFileType:int = obj["StructuredOutputFileType"]
      """  StructuredOutputFileType  """  
      self.OutputLocation:str = obj["OutputLocation"]
      """  OutputLocation  """  
      self.OutputColumnHeaders:bool = obj["OutputColumnHeaders"]
      """  OutputColumnHeaders  """  
      self.AdditionalSettings:str = obj["AdditionalSettings"]
      """  AdditionalSettings  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AttachToPDFA3:bool = obj["AttachToPDFA3"]
      """  AttachToPDFA3  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStructuredOutputFileXMLNSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputFileID:str = obj["RptStructuredOutputFileID"]
      """  RptStructuredOutputFileID  """  
      self.RptStructuredOutputFileNamespaceID:int = obj["RptStructuredOutputFileNamespaceID"]
      """  RptStructuredOutputFileNamespaceID  """  
      self.Namespace:str = obj["Namespace"]
      """  Namespace  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteAllOutputFileElements_input:
   """ Required : 
   structuredDefID
   structuredDefFileID
   """  
   def __init__(self, obj):
      self.structuredDefID:str = obj["structuredDefID"]
      """  The structured definition identifier.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  The structured definition file identifier.  """  
      pass

class DeleteAllOutputFileElements_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   rptStructuredOutputDefID
   """  
   def __init__(self, obj):
      self.rptStructuredOutputDefID:str = obj["rptStructuredOutputDefID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DescendantsWithDataSourceIdExist_input:
   """ Required : 
   structuredDefTS
   structuredDefID
   structuredDefFileID
   elementID
   originalDataSourceId
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      self.structuredDefID:str = obj["structuredDefID"]
      """  RptStructuredOutputDefID value.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  RptStructuredOutputFileID value.  """  
      self.elementID:int = obj["elementID"]
      """  ElementID value.  """  
      self.originalDataSourceId:str = obj["originalDataSourceId"]
      """  original DataSourceId value  """  
      pass

class DescendantsWithDataSourceIdExist_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

class DuplicateStructuredOutputDef_input:
   """ Required : 
   sourceSOutputDefID
   targetSOutputDefID
   targetSOutputDefDesc
   """  
   def __init__(self, obj):
      self.sourceSOutputDefID:str = obj["sourceSOutputDefID"]
      self.targetSOutputDefID:str = obj["targetSOutputDefID"]
      self.targetSOutputDefDesc:str = obj["targetSOutputDefDesc"]
      pass

class DuplicateStructuredOutputDef_output:
   def __init__(self, obj):
      pass

class DuplicateStructuredOutputFile_input:
   """ Required : 
   sourceSOutputDefID
   sourceSOutputFileID
   targetSOutputDefID
   targetSOutputFileID
   targetSOutputFileDesc
   """  
   def __init__(self, obj):
      self.sourceSOutputDefID:str = obj["sourceSOutputDefID"]
      self.sourceSOutputFileID:str = obj["sourceSOutputFileID"]
      self.targetSOutputDefID:str = obj["targetSOutputDefID"]
      self.targetSOutputFileID:str = obj["targetSOutputFileID"]
      self.targetSOutputFileDesc:str = obj["targetSOutputFileDesc"]
      pass

class DuplicateStructuredOutputFile_output:
   def __init__(self, obj):
      pass

class GetAncestorDataSource_input:
   """ Required : 
   structuredDefID
   structuredDefFileID
   elementID
   """  
   def __init__(self, obj):
      self.structuredDefID:str = obj["structuredDefID"]
      """  RptStructuredOutputDefID value.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  RptStructuredOutputFileID value.  """  
      self.elementID:int = obj["elementID"]
      """  ElementID value.  """  
      pass

class GetAncestorDataSource_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   rptStructuredOutputDefID
   """  
   def __init__(self, obj):
      self.rptStructuredOutputDefID:str = obj["rptStructuredOutputDefID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["returnObj"]
      pass

class GetDataSourceColumnType_input:
   """ Required : 
   rptDefID
   dataSourceId
   columnName
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      """  Report data definition id.  """  
      self.dataSourceId:str = obj["dataSourceId"]
      """  Data source id.  """  
      self.columnName:str = obj["columnName"]
      """  Data source column name.  """  
      pass

class GetDataSourceColumnType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDataSourceColumns_input:
   """ Required : 
   structuredDefID
   dataSourceID
   """  
   def __init__(self, obj):
      self.structuredDefID:str = obj["structuredDefID"]
      """  RptStructuredOutputDefID value.  """  
      self.dataSourceID:str = obj["dataSourceID"]
      """  Data source id.  """  
      pass

class GetDataSourceColumns_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptDataSourceTableset] = obj["returnObj"]
      pass

class GetDataSourceListWithIsUsedSet_input:
   """ Required : 
   structuredDefID
   structuredDefFileID
   elementID
   """  
   def __init__(self, obj):
      self.structuredDefID:str = obj["structuredDefID"]
      """  RptStructuredOutputDefID value.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  RptStructuredOutputFileID value.  """  
      self.elementID:int = obj["elementID"]
      """  ElementID value.  """  
      pass

class GetDataSourceListWithIsUsedSet_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptDataSourceTableset] = obj["returnObj"]
      pass

class GetDataSourceList_input:
   """ Required : 
   structuredDefID
   structuredDefFileID
   elementID
   """  
   def __init__(self, obj):
      self.structuredDefID:str = obj["structuredDefID"]
      """  RptStructuredOutputDefID value.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  RptStructuredOutputFileID value.  """  
      self.elementID:int = obj["elementID"]
      """  ElementID value.  """  
      pass

class GetDataSourceList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptDataSourceTableset] = obj["returnObj"]
      pass

class GetEICalculators_input:
   """ Required : 
   eFTHeadCompany
   eFTHeadUID
   currentCalculationName
   """  
   def __init__(self, obj):
      self.eFTHeadCompany:str = obj["eFTHeadCompany"]
      self.eFTHeadUID:int = obj["eFTHeadUID"]
      self.currentCalculationName:str = obj["currentCalculationName"]
      """  Current CalculationName value  """  
      pass

class GetEICalculators_output:
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
      self.returnObj:list[Ice_Tablesets_RptStructuredOutputDefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRptStructuredOutputDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      pass

class GetNewRptStructuredOutputDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptStructuredOutputFileElement_input:
   """ Required : 
   ds
   rptStructuredOutputDefID
   rptStructuredOutputFileID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      self.rptStructuredOutputDefID:str = obj["rptStructuredOutputDefID"]
      self.rptStructuredOutputFileID:str = obj["rptStructuredOutputFileID"]
      pass

class GetNewRptStructuredOutputFileElement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptStructuredOutputFileXMLNS_input:
   """ Required : 
   ds
   rptStructuredOutputDefID
   rptStructuredOutputFileID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      self.rptStructuredOutputDefID:str = obj["rptStructuredOutputDefID"]
      self.rptStructuredOutputFileID:str = obj["rptStructuredOutputFileID"]
      pass

class GetNewRptStructuredOutputFileXMLNS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptStructuredOutputFile_input:
   """ Required : 
   ds
   rptStructuredOutputDefID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      self.rptStructuredOutputDefID:str = obj["rptStructuredOutputDefID"]
      pass

class GetNewRptStructuredOutputFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRptStructuredOutputDef
   whereClauseRptStructuredOutputFile
   whereClauseRptStructuredOutputFileElement
   whereClauseRptStructuredOutputFileXMLNS
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRptStructuredOutputDef:str = obj["whereClauseRptStructuredOutputDef"]
      self.whereClauseRptStructuredOutputFile:str = obj["whereClauseRptStructuredOutputFile"]
      self.whereClauseRptStructuredOutputFileElement:str = obj["whereClauseRptStructuredOutputFileElement"]
      self.whereClauseRptStructuredOutputFileXMLNS:str = obj["whereClauseRptStructuredOutputFileXMLNS"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["returnObj"]
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

class Ice_Tablesets_RptDataSourceColumnRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      self.DataSourceID:str = obj["DataSourceID"]
      self.ColumnName:str = obj["ColumnName"]
      self.DataType:str = obj["DataType"]
      self.ColumnAlias:str = obj["ColumnAlias"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataSourceRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      self.DataSourceID:str = obj["DataSourceID"]
      self.IsUsed:bool = obj["IsUsed"]
      self.NeedSign:str = obj["NeedSign"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataSourceTableset:
   def __init__(self, obj):
      self.RptDataSource:list[Ice_Tablesets_RptDataSourceRow] = obj["RptDataSource"]
      self.RptDataSourceColumn:list[Ice_Tablesets_RptDataSourceColumnRow] = obj["RptDataSourceColumn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptStructuredOutputDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputDescription:str = obj["RptStructuredOutputDescription"]
      """  RptStructuredOutputDescription  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.ConfirmedCompliance:bool = obj["ConfirmedCompliance"]
      """  ConfirmedCompliance  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RptDataDefRptDescription:str = obj["RptDataDefRptDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStructuredOutputDefListTableset:
   def __init__(self, obj):
      self.RptStructuredOutputDefList:list[Ice_Tablesets_RptStructuredOutputDefListRow] = obj["RptStructuredOutputDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptStructuredOutputDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputDescription:str = obj["RptStructuredOutputDescription"]
      """  RptStructuredOutputDescription  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.ConfirmedCompliance:bool = obj["ConfirmedCompliance"]
      """  ConfirmedCompliance  """  
      self.ComplianceRule:str = obj["ComplianceRule"]
      """  ComplianceRule  """  
      self.InternalComments:str = obj["InternalComments"]
      """  InternalComments  """  
      self.DateFormat:str = obj["DateFormat"]
      """  DateFormat  """  
      self.DecimalSymbol:str = obj["DecimalSymbol"]
      """  DecimalSymbol  """  
      self.DigitGroupingSymbol:str = obj["DigitGroupingSymbol"]
      """  DigitGroupingSymbol  """  
      self.NegativeSignSymbol:str = obj["NegativeSignSymbol"]
      """  NegativeSignSymbol  """  
      self.Encoding:str = obj["Encoding"]
      """  Encoding  """  
      self.Delimiter:str = obj["Delimiter"]
      """  Delimiter  """  
      self.EndOfRecordSymbol:str = obj["EndOfRecordSymbol"]
      """  EndOfRecordSymbol  """  
      self.QuotationMark:str = obj["QuotationMark"]
      """  QuotationMark  """  
      self.QuoteAllValues:bool = obj["QuoteAllValues"]
      """  QuoteAllValues  """  
      self.BooleanTrue:str = obj["BooleanTrue"]
      """  BooleanTrue  """  
      self.BooleanFalse:str = obj["BooleanFalse"]
      """  BooleanFalse  """  
      self.PrePostProcessingEFTHeadCompany:str = obj["PrePostProcessingEFTHeadCompany"]
      """  PrePostProcessingEFTHeadCompany  """  
      self.PrePostProcessingEFTHeadUID:int = obj["PrePostProcessingEFTHeadUID"]
      """  PrePostProcessingEFTHeadUID  """  
      self.AdditionalSettings:str = obj["AdditionalSettings"]
      """  AdditionalSettings  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PrePostProcessingDescription:str = obj["PrePostProcessingDescription"]
      """  Description for the PrePostProcessingEFTHeadUID  """  
      self.PrePostProcessingName:str = obj["PrePostProcessingName"]
      """  Name of the PrePostProcessingEFTHeadUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RptDataDefSystemRpt:bool = obj["RptDataDefSystemRpt"]
      self.RptDataDefRptDescription:str = obj["RptDataDefRptDescription"]
      self.RptDataDefDuplicateOf:str = obj["RptDataDefDuplicateOf"]
      self.RptDataDefRptTypeID:str = obj["RptDataDefRptTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStructuredOutputDefTableset:
   def __init__(self, obj):
      self.RptStructuredOutputDef:list[Ice_Tablesets_RptStructuredOutputDefRow] = obj["RptStructuredOutputDef"]
      self.RptStructuredOutputFile:list[Ice_Tablesets_RptStructuredOutputFileRow] = obj["RptStructuredOutputFile"]
      self.RptStructuredOutputFileElement:list[Ice_Tablesets_RptStructuredOutputFileElementRow] = obj["RptStructuredOutputFileElement"]
      self.RptStructuredOutputFileXMLNS:list[Ice_Tablesets_RptStructuredOutputFileXMLNSRow] = obj["RptStructuredOutputFileXMLNS"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptStructuredOutputFileElementRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputFileID:str = obj["RptStructuredOutputFileID"]
      """  RptStructuredOutputFileID  """  
      self.ElementID:int = obj["ElementID"]
      """  ElementID  """  
      self.ElementName:str = obj["ElementName"]
      """  ElementName  """  
      self.ParentElementID:int = obj["ParentElementID"]
      """  ParentElementID  """  
      self.ChildSequence:int = obj["ChildSequence"]
      """  ChildSequence  """  
      self.Namespace:str = obj["Namespace"]
      """  Namespace  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.XMLAttribute:bool = obj["XMLAttribute"]
      """  XMLAttribute  """  
      self.AggregationType:int = obj["AggregationType"]
      """  AggregationType  """  
      self.DecimalScale:int = obj["DecimalScale"]
      """  DecimalScale  """  
      self.DataSourceID:str = obj["DataSourceID"]
      """  DataSourceID  """  
      self.DataSourceColumn:str = obj["DataSourceColumn"]
      """  DataSourceColumn  """  
      self.IsConstant:bool = obj["IsConstant"]
      """  IsConstant  """  
      self.ConstantValue:str = obj["ConstantValue"]
      """  ConstantValue  """  
      self.CalculationEFTHeadCompany:str = obj["CalculationEFTHeadCompany"]
      """  CalculationEFTHeadCompany  """  
      self.CalculationEFTHeadUID:int = obj["CalculationEFTHeadUID"]
      """  CalculationEFTHeadUID  """  
      self.CalculationName:str = obj["CalculationName"]
      """  CalculationName  """  
      self.AdditionalSettings:str = obj["AdditionalSettings"]
      """  AdditionalSettings  """  
      self.DateFormat:str = obj["DateFormat"]
      """  DateFormat  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.JSONObject:bool = obj["JSONObject"]
      """  JSONObject  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ElementDataType:str = obj["ElementDataType"]
      """  ElementDataType  """  
      self.ElementDescription:str = obj["ElementDescription"]
      """  ElementDescription  """  
      self.EmptyStringGenerateEmptyElement:bool = obj["EmptyStringGenerateEmptyElement"]
      """  EmptyStringGenerateEmptyElement  """  
      self.EmptyStringSuppressOrNullElement:bool = obj["EmptyStringSuppressOrNullElement"]
      """  EmptyStringSuppressOrNullElement  """  
      self.EmptyStringSubsituteElement:bool = obj["EmptyStringSubsituteElement"]
      """  EmptyStringSubsituteElement  """  
      self.EmptyStringSubsituteValue:str = obj["EmptyStringSubsituteValue"]
      """  EmptyStringSubsituteValue  """  
      self.ZeroNumericSuppress:bool = obj["ZeroNumericSuppress"]
      """  ZeroNumericSuppress  """  
      self.NeedSign:bool = obj["NeedSign"]
      """  NeedSign  """  
      self.CalculationEFTHeadName:str = obj["CalculationEFTHeadName"]
      """  CalculationEFTHeadName  """  
      self.DataSourceColumnDataType:str = obj["DataSourceColumnDataType"]
      """  .NET Data type for the datasource column.  """  
      self.ElementFullName:str = obj["ElementFullName"]
      """  Element name including the prefix. Prefix:ElementName or ElementName if Prefix=""  """  
      self.ValidationErrorColumns:str = obj["ValidationErrorColumns"]
      """  List of table columns with validation rules.  """  
      self.ValidationMessage:str = obj["ValidationMessage"]
      """  Validation message from all columns.  """  
      self.IsDocLevelPrefix:bool = obj["IsDocLevelPrefix"]
      """  Is Doc Level Prefix  """  
      self.DocLevelNamespace:str = obj["DocLevelNamespace"]
      """  Doc Level Namespace  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStructuredOutputFileRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputFileID:str = obj["RptStructuredOutputFileID"]
      """  RptStructuredOutputFileID  """  
      self.RptStructuredOutputFileDesc:str = obj["RptStructuredOutputFileDesc"]
      """  RptStructuredOutputFileDesc  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled  """  
      self.StructuredOutputFileType:int = obj["StructuredOutputFileType"]
      """  StructuredOutputFileType  """  
      self.OutputLocation:str = obj["OutputLocation"]
      """  OutputLocation  """  
      self.OutputColumnHeaders:bool = obj["OutputColumnHeaders"]
      """  OutputColumnHeaders  """  
      self.AdditionalSettings:str = obj["AdditionalSettings"]
      """  AdditionalSettings  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AttachToPDFA3:bool = obj["AttachToPDFA3"]
      """  AttachToPDFA3  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStructuredOutputFileXMLNSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.RptStructuredOutputFileID:str = obj["RptStructuredOutputFileID"]
      """  RptStructuredOutputFileID  """  
      self.RptStructuredOutputFileNamespaceID:int = obj["RptStructuredOutputFileNamespaceID"]
      """  RptStructuredOutputFileNamespaceID  """  
      self.Namespace:str = obj["Namespace"]
      """  Namespace  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtRptStructuredOutputDefTableset:
   def __init__(self, obj):
      self.RptStructuredOutputDef:list[Ice_Tablesets_RptStructuredOutputDefRow] = obj["RptStructuredOutputDef"]
      self.RptStructuredOutputFile:list[Ice_Tablesets_RptStructuredOutputFileRow] = obj["RptStructuredOutputFile"]
      self.RptStructuredOutputFileElement:list[Ice_Tablesets_RptStructuredOutputFileElementRow] = obj["RptStructuredOutputFileElement"]
      self.RptStructuredOutputFileXMLNS:list[Ice_Tablesets_RptStructuredOutputFileXMLNSRow] = obj["RptStructuredOutputFileXMLNS"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportFile_input:
   """ Required : 
   structuredDefTS
   structuredDefID
   structuredDefFileID
   method
   filePath
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      self.structuredDefID:str = obj["structuredDefID"]
      """  The structured definition identifier.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  The structured definition file identifier.  """  
      self.method:str = obj["method"]
      """  The import method name.  """  
      self.filePath:str = obj["filePath"]
      """  The file path.  """  
      pass

class ImportFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

class ImportJSONSchema_input:
   """ Required : 
   structuredDefTS
   structuredDefID
   structuredDefFileID
   jsonSchema
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      self.structuredDefID:str = obj["structuredDefID"]
      """  The structured definition identifier.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  The structured definition file identifier.  """  
      self.jsonSchema:str = obj["jsonSchema"]
      """  The json schema.  """  
      pass

class ImportJSONSchema_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

class ImportXmlDataWithNoValues_input:
   """ Required : 
   structuredDefTS
   structuredDefID
   structuredDefFileID
   xmlData
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      self.structuredDefID:str = obj["structuredDefID"]
      """  The structured definition identifier.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  The structured definition file identifier.  """  
      self.xmlData:str = obj["xmlData"]
      """  The XML data.  """  
      pass

class ImportXmlDataWithNoValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

class ImportXmlDataWithValues_input:
   """ Required : 
   structuredDefTS
   structuredDefID
   structuredDefFileID
   xmlData
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      self.structuredDefID:str = obj["structuredDefID"]
      """  The structured definition identifier.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  The structured definition file identifier.  """  
      self.xmlData:str = obj["xmlData"]
      """  The XML data.  """  
      pass

class ImportXmlDataWithValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

class OnChangeOutputLocation_input:
   """ Required : 
   reportId
   proposedOutputLocation
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report ID.  """  
      self.proposedOutputLocation:str = obj["proposedOutputLocation"]
      """  The proposed output location.  """  
      pass

class OnChangeOutputLocation_output:
   def __init__(self, obj):
      pass

class OnChangeReportDataDefinition_input:
   """ Required : 
   structuredDefTS
   proposedRptDefId
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      self.proposedRptDefId:str = obj["proposedRptDefId"]
      """  The proposed Report Data Definition identifier.  """  
      pass

class OnChangeReportDataDefinition_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

class UpdateDescendantsWithNewDataSourceId_input:
   """ Required : 
   structuredDefTS
   structuredDefID
   structuredDefFileID
   elementID
   originalDataSourceId
   newDataSourceID
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      self.structuredDefID:str = obj["structuredDefID"]
      """  RptStructuredOutputDefID value.  """  
      self.structuredDefFileID:str = obj["structuredDefFileID"]
      """  RptStructuredOutputFileID value.  """  
      self.elementID:int = obj["elementID"]
      """  ElementID value.  """  
      self.originalDataSourceId:str = obj["originalDataSourceId"]
      """  original DataSourceId value  """  
      self.newDataSourceID:str = obj["newDataSourceID"]
      """  new DataSourceID value  """  
      pass

class UpdateDescendantsWithNewDataSourceId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtRptStructuredOutputDefTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtRptStructuredOutputDefTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOutputFileElement_input:
   """ Required : 
   structuredDefTS
   elementToValidate
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      self.elementToValidate:int = obj["elementToValidate"]
      """  >ElementID of output file element row to validate.  """  
      pass

class ValidateOutputFileElement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

class ValidateOutputFileElements_input:
   """ Required : 
   structuredDefTS
   """  
   def __init__(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

class ValidateOutputFileElements_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.structuredDefTS:list[Ice_Tablesets_RptStructuredOutputDefTableset] = obj["structuredDefTS"]
      pass

      """  output parameters  """  

