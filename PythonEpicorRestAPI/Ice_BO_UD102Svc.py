import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.UD102Svc
# Description: User Defined Table 102
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_UD102s(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UD102s items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UD102s
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD102Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s",headers=creds) as resp:
           return await resp.json()

async def post_UD102s(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UD102s
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UD102Row
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UD102Row
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UD102s_Company_Key1_Key2_Key3_Key4_Key5(Company, Key1, Key2, Key3, Key4, Key5, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD102 item
   Description: Calls GetByID to retrieve the UD102 item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD102
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD102Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UD102s_Company_Key1_Key2_Key3_Key4_Key5(Company, Key1, Key2, Key3, Key4, Key5, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UD102 for the service
   Description: Calls UpdateExt to update UD102. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UD102
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UD102Row
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UD102s_Company_Key1_Key2_Key3_Key4_Key5(Company, Key1, Key2, Key3, Key4, Key5, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UD102 item
   Description: Call UpdateExt to delete UD102 item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UD102
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_UD102s_Company_Key1_Key2_Key3_Key4_Key5_UD102As(Company, Key1, Key2, Key3, Key4, Key5, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UD102As items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UD102As1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD102ARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/UD102As",headers=creds) as resp:
           return await resp.json()

async def get_UD102s_Company_Key1_Key2_Key3_Key4_Key5_UD102As_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD102A item
   Description: Calls GetByID to retrieve the UD102A item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD102A1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD102ARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/UD102As(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_UD102s_Company_Key1_Key2_Key3_Key4_Key5_UD102Attchs(Company, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UD102Attchs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UD102Attchs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD102AttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/UD102Attchs",headers=creds) as resp:
           return await resp.json()

async def get_UD102s_Company_Key1_Key2_Key3_Key4_Key5_UD102Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD102Attch item
   Description: Calls GetByID to retrieve the UD102Attch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD102Attch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD102AttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/UD102Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_UD102As(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UD102As items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UD102As
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD102ARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102As",headers=creds) as resp:
           return await resp.json()

async def post_UD102As(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UD102As
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UD102ARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UD102ARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102As", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UD102As_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD102A item
   Description: Calls GetByID to retrieve the UD102A item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD102A
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD102ARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102As(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UD102As_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UD102A for the service
   Description: Calls UpdateExt to update UD102A. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UD102A
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UD102ARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102As(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UD102As_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UD102A item
   Description: Call UpdateExt to delete UD102A item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UD102A
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102As(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_UD102As_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5_UD102AAttchs(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UD102AAttchs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UD102AAttchs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD102AAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102As(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + ")/UD102AAttchs",headers=creds) as resp:
           return await resp.json()

async def get_UD102As_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5_UD102AAttchs_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD102AAttch item
   Description: Calls GetByID to retrieve the UD102AAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD102AAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD102AAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102As(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + ")/UD102AAttchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_UD102AAttchs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UD102AAttchs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UD102AAttchs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD102AAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102AAttchs",headers=creds) as resp:
           return await resp.json()

async def post_UD102AAttchs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UD102AAttchs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UD102AAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UD102AAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102AAttchs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UD102AAttchs_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD102AAttch item
   Description: Calls GetByID to retrieve the UD102AAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD102AAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD102AAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102AAttchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UD102AAttchs_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UD102AAttch for the service
   Description: Calls UpdateExt to update UD102AAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UD102AAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UD102AAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102AAttchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UD102AAttchs_Company_Key1_Key2_Key3_Key4_Key5_ChildKey1_ChildKey2_ChildKey3_ChildKey4_ChildKey5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, ChildKey1, ChildKey2, ChildKey3, ChildKey4, ChildKey5, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UD102AAttch item
   Description: Call UpdateExt to delete UD102AAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UD102AAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param ChildKey1: Desc: ChildKey1   Required: True   Allow empty value : True
      :param ChildKey2: Desc: ChildKey2   Required: True   Allow empty value : True
      :param ChildKey3: Desc: ChildKey3   Required: True   Allow empty value : True
      :param ChildKey4: Desc: ChildKey4   Required: True   Allow empty value : True
      :param ChildKey5: Desc: ChildKey5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102AAttchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + ChildKey1 + "," + ChildKey2 + "," + ChildKey3 + "," + ChildKey4 + "," + ChildKey5 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_UD102Attchs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UD102Attchs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UD102Attchs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD102AttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102Attchs",headers=creds) as resp:
           return await resp.json()

async def post_UD102Attchs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UD102Attchs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UD102AttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UD102AttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102Attchs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UD102Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD102Attch item
   Description: Calls GetByID to retrieve the UD102Attch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD102Attch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD102AttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UD102Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UD102Attch for the service
   Description: Calls UpdateExt to update UD102Attch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UD102Attch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UD102AttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UD102Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UD102Attch item
   Description: Call UpdateExt to delete UD102Attch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UD102Attch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/UD102Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD102ListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseUD102, whereClauseUD102Attch, whereClauseUD102A, whereClauseUD102AAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseUD102=" + whereClauseUD102
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUD102Attch=" + whereClauseUD102Attch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUD102A=" + whereClauseUD102A
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUD102AAttch=" + whereClauseUD102AAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(key1, key2, key3, key4, key5, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key4=" + key4
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key5=" + key5

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetaNewUD102(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetaNewUD102
   Description: Get new for UD102.
   OperationID: GetaNewUD102
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetaNewUD102_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetaNewUD102_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetaNewUD102A(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetaNewUD102A
   Description: Get new for UD102A.
   OperationID: GetaNewUD102A
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetaNewUD102A_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetaNewUD102A_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUD102(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUD102
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUD102
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUD102_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUD102_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUD102Attch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUD102Attch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUD102Attch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUD102Attch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUD102Attch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUD102A(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUD102A
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUD102A
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUD102A_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUD102A_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUD102AAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUD102AAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUD102AAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUD102AAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUD102AAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD102Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD102AAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UD102AAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD102ARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UD102ARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD102AttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UD102AttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD102ListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UD102ListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD102Row:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UD102Row] = obj["value"]
      pass

class Ice_Tablesets_UD102AAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.ChildKey1:str = obj["ChildKey1"]
      self.ChildKey2:str = obj["ChildKey2"]
      self.ChildKey3:str = obj["ChildKey3"]
      self.ChildKey4:str = obj["ChildKey4"]
      self.ChildKey5:str = obj["ChildKey5"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102ARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.ChildKey1:str = obj["ChildKey1"]
      """  ChildKey1  """  
      self.ChildKey2:str = obj["ChildKey2"]
      """  ChildKey2  """  
      self.ChildKey3:str = obj["ChildKey3"]
      """  ChildKey3  """  
      self.ChildKey4:str = obj["ChildKey4"]
      """  ChildKey4  """  
      self.ChildKey5:str = obj["ChildKey5"]
      """  ChildKey5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.GlobalUD102A:bool = obj["GlobalUD102A"]
      """  GlobalUD102A  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102AttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102ListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.GlobalUD102:bool = obj["GlobalUD102"]
      """  GlobalUD102  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.GlobalUD102:bool = obj["GlobalUD102"]
      """  GlobalUD102  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
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
class DeleteByID_input:
   """ Required : 
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UD102Tableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_UD102Tableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_UD102Tableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_UD102ListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewUD102AAttch_input:
   """ Required : 
   ds
   key1
   key2
   key3
   key4
   key5
   childKey1
   childKey2
   childKey3
   childKey4
   childKey5
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.childKey1:str = obj["childKey1"]
      self.childKey2:str = obj["childKey2"]
      self.childKey3:str = obj["childKey3"]
      self.childKey4:str = obj["childKey4"]
      self.childKey5:str = obj["childKey5"]
      pass

class GetNewUD102AAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUD102A_input:
   """ Required : 
   ds
   key1
   key2
   key3
   key4
   key5
   childKey1
   childKey2
   childKey3
   childKey4
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.childKey1:str = obj["childKey1"]
      self.childKey2:str = obj["childKey2"]
      self.childKey3:str = obj["childKey3"]
      self.childKey4:str = obj["childKey4"]
      pass

class GetNewUD102A_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUD102Attch_input:
   """ Required : 
   ds
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class GetNewUD102Attch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUD102_input:
   """ Required : 
   ds
   key1
   key2
   key3
   key4
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      pass

class GetNewUD102_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseUD102
   whereClauseUD102Attch
   whereClauseUD102A
   whereClauseUD102AAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseUD102:str = obj["whereClauseUD102"]
      self.whereClauseUD102Attch:str = obj["whereClauseUD102Attch"]
      self.whereClauseUD102A:str = obj["whereClauseUD102A"]
      self.whereClauseUD102AAttch:str = obj["whereClauseUD102AAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UD102Tableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetaNewUD102A_input:
   """ Required : 
   ds
   ParentKey1
   ParentKey2
   ParentKey3
   ParentKey4
   ParentKey5
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      self.ParentKey1:str = obj["ParentKey1"]
      """  Parent key1  """  
      self.ParentKey2:str = obj["ParentKey2"]
      """  Parent key2  """  
      self.ParentKey3:str = obj["ParentKey3"]
      """  Parent key3  """  
      self.ParentKey4:str = obj["ParentKey4"]
      """  Parent key4  """  
      self.ParentKey5:str = obj["ParentKey5"]
      """  Parent key5  """  
      pass

class GetaNewUD102A_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetaNewUD102_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      pass

class GetaNewUD102_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
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

class Ice_Tablesets_UD102AAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.ChildKey1:str = obj["ChildKey1"]
      self.ChildKey2:str = obj["ChildKey2"]
      self.ChildKey3:str = obj["ChildKey3"]
      self.ChildKey4:str = obj["ChildKey4"]
      self.ChildKey5:str = obj["ChildKey5"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102ARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.ChildKey1:str = obj["ChildKey1"]
      """  ChildKey1  """  
      self.ChildKey2:str = obj["ChildKey2"]
      """  ChildKey2  """  
      self.ChildKey3:str = obj["ChildKey3"]
      """  ChildKey3  """  
      self.ChildKey4:str = obj["ChildKey4"]
      """  ChildKey4  """  
      self.ChildKey5:str = obj["ChildKey5"]
      """  ChildKey5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.GlobalUD102A:bool = obj["GlobalUD102A"]
      """  GlobalUD102A  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102AttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102ListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.GlobalUD102:bool = obj["GlobalUD102"]
      """  GlobalUD102  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102ListTableset:
   def __init__(self, obj):
      self.UD102List:list[Ice_Tablesets_UD102ListRow] = obj["UD102List"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UD102Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.GlobalUD102:bool = obj["GlobalUD102"]
      """  GlobalUD102  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD102Tableset:
   def __init__(self, obj):
      self.UD102:list[Ice_Tablesets_UD102Row] = obj["UD102"]
      self.UD102Attch:list[Ice_Tablesets_UD102AttchRow] = obj["UD102Attch"]
      self.UD102A:list[Ice_Tablesets_UD102ARow] = obj["UD102A"]
      self.UD102AAttch:list[Ice_Tablesets_UD102AAttchRow] = obj["UD102AAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtUD102Tableset:
   def __init__(self, obj):
      self.UD102:list[Ice_Tablesets_UD102Row] = obj["UD102"]
      self.UD102Attch:list[Ice_Tablesets_UD102AttchRow] = obj["UD102Attch"]
      self.UD102A:list[Ice_Tablesets_UD102ARow] = obj["UD102A"]
      self.UD102AAttch:list[Ice_Tablesets_UD102AAttchRow] = obj["UD102AAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtUD102Tableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtUD102Tableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD102Tableset] = obj["ds"]
      pass

      """  output parameters  """  

