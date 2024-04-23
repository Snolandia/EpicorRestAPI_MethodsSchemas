import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ExtCompanySvc
# Description: ExtCompany object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanies
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company, ExtSystemID, ExtCompanyID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompany item
   Description: Calls GetByID to retrieve the ExtCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompany
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company, ExtSystemID, ExtCompanyID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompany for the service
   Description: Calls UpdateExt to update ExtCompany. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompany
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanies_Company_ExtSystemID_ExtCompanyID(Company, ExtSystemID, ExtCompanyID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompany item
   Description: Call UpdateExt to delete ExtCompany item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompany
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtCompanyECCs(Company, ExtSystemID, ExtCompanyID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtCompanyECCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtCompanyECCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyECCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtCompanyECCs",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID(Company, ExtSystemID, ExtCompanyID, ECCID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyECC item
   Description: Calls GetByID to retrieve the ExtCompanyECC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyECC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtPlants(Company, ExtSystemID, ExtCompanyID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtPlants items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtPlants1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtPlants",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID(Company, ExtSystemID, ExtCompanyID, TransferMethod, ExtPlantID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPlant item
   Description: Calls GetByID to retrieve the ExtPlant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPlant1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_EntityGLCs(Company, ExtSystemID, ExtCompanyID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, ExtSystemID, ExtCompanyID, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtCompanyAttches(Company, ExtSystemID, ExtCompanyID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtCompanyAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtCompanyAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtCompanyAttches",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanies_Company_ExtSystemID_ExtCompanyID_ExtCompanyAttches_Company_ExtSystemID_ExtCompanyID_DrawingSeq(Company, ExtSystemID, ExtCompanyID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyAttch item
   Description: Calls GetByID to retrieve the ExtCompanyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanies(" + Company + "," + ExtSystemID + "," + ExtCompanyID + ")/ExtCompanyAttches(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyECCs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyECCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyECCs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyECCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanyECCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyECCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID(Company, ExtCompanyID, ExtSystemID, ECCID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyECC item
   Description: Calls GetByID to retrieve the ExtCompanyECC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyECC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID(Company, ExtCompanyID, ExtSystemID, ECCID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompanyECC for the service
   Description: Calls UpdateExt to update ExtCompanyECC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyECC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyECCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID(Company, ExtCompanyID, ExtSystemID, ECCID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompanyECC item
   Description: Call UpdateExt to delete ExtCompanyECC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyECC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID_ECCDocTypes(Company, ExtCompanyID, ExtSystemID, ECCID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECCDocTypes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECCDocTypes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")/ECCDocTypes",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID_ECCDocTypes_Company_ExtCompanyID_ExtSystemID_ECCID_DocTypeID(Company, ExtCompanyID, ExtSystemID, ECCID, DocTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECCDocType item
   Description: Calls GetByID to retrieve the ECCDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCDocType1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param DocTypeID: Desc: DocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")/ECCDocTypes(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + DocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID_ECCReportDefaultStyles(Company, ExtCompanyID, ExtSystemID, ECCID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECCReportDefaultStyles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECCReportDefaultStyles1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCReportDefaultStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")/ECCReportDefaultStyles",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyECCs_Company_ExtCompanyID_ExtSystemID_ECCID_ECCReportDefaultStyles_Company_ExtCompanyID_ExtSystemID_ECCID_AutoProgram(Company, ExtCompanyID, ExtSystemID, ECCID, AutoProgram, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECCReportDefaultStyle item
   Description: Calls GetByID to retrieve the ECCReportDefaultStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCReportDefaultStyle1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param AutoProgram: Desc: AutoProgram   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyECCs(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + ")/ECCReportDefaultStyles(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + AutoProgram + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECCDocTypes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECCDocTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECCDocTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes",headers=creds) as resp:
           return await resp.json()

async def post_ECCDocTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECCDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECCDocTypes_Company_ExtCompanyID_ExtSystemID_ECCID_DocTypeID(Company, ExtCompanyID, ExtSystemID, ECCID, DocTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECCDocType item
   Description: Calls GetByID to retrieve the ECCDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param DocTypeID: Desc: DocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + DocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECCDocTypes_Company_ExtCompanyID_ExtSystemID_ECCID_DocTypeID(Company, ExtCompanyID, ExtSystemID, ECCID, DocTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECCDocType for the service
   Description: Calls UpdateExt to update ECCDocType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECCDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param DocTypeID: Desc: DocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECCDocTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + DocTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECCDocTypes_Company_ExtCompanyID_ExtSystemID_ECCID_DocTypeID(Company, ExtCompanyID, ExtSystemID, ECCID, DocTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECCDocType item
   Description: Call UpdateExt to delete ECCDocType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECCDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param DocTypeID: Desc: DocTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCDocTypes(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + DocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECCReportDefaultStyles(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECCReportDefaultStyles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECCReportDefaultStyles
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCReportDefaultStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles",headers=creds) as resp:
           return await resp.json()

async def post_ECCReportDefaultStyles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECCReportDefaultStyles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECCReportDefaultStyles_Company_ExtCompanyID_ExtSystemID_ECCID_AutoProgram(Company, ExtCompanyID, ExtSystemID, ECCID, AutoProgram, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECCReportDefaultStyle item
   Description: Calls GetByID to retrieve the ECCReportDefaultStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCReportDefaultStyle
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param AutoProgram: Desc: AutoProgram   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + AutoProgram + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECCReportDefaultStyles_Company_ExtCompanyID_ExtSystemID_ECCID_AutoProgram(Company, ExtCompanyID, ExtSystemID, ECCID, AutoProgram, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECCReportDefaultStyle for the service
   Description: Calls UpdateExt to update ECCReportDefaultStyle. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECCReportDefaultStyle
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param AutoProgram: Desc: AutoProgram   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECCReportDefaultStyleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + AutoProgram + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECCReportDefaultStyles_Company_ExtCompanyID_ExtSystemID_ECCID_AutoProgram(Company, ExtCompanyID, ExtSystemID, ECCID, AutoProgram, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECCReportDefaultStyle item
   Description: Call UpdateExt to delete ECCReportDefaultStyle item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECCReportDefaultStyle
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ECCID: Desc: ECCID   Required: True
      :param AutoProgram: Desc: AutoProgram   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ECCReportDefaultStyles(" + Company + "," + ExtCompanyID + "," + ExtSystemID + "," + ECCID + "," + AutoProgram + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPlants(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtPlants items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPlants
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants",headers=creds) as resp:
           return await resp.json()

async def post_ExtPlants(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPlants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPlant item
   Description: Calls GetByID to retrieve the ExtPlant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPlant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtPlant for the service
   Description: Calls UpdateExt to update ExtPlant. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPlant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtPlant item
   Description: Call UpdateExt to delete ExtPlant item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPlant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouses(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtWarehouses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtWarehouses1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtWarehouseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")/ExtWarehouses",headers=creds) as resp:
           return await resp.json()

async def get_ExtPlants_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouses_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, ExtWarehouseID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtWarehouse item
   Description: Calls GetByID to retrieve the ExtWarehouse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtWarehouse1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param ExtWarehouseID: Desc: ExtWarehouseID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtPlants(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + ")/ExtWarehouses(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtWarehouses(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtWarehouses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtWarehouses
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtWarehouseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses",headers=creds) as resp:
           return await resp.json()

async def post_ExtWarehouses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtWarehouses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtWarehouses_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, ExtWarehouseID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtWarehouse item
   Description: Calls GetByID to retrieve the ExtWarehouse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtWarehouse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param ExtWarehouseID: Desc: ExtWarehouseID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtWarehouses_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, ExtWarehouseID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtWarehouse for the service
   Description: Calls UpdateExt to update ExtWarehouse. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtWarehouse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param ExtWarehouseID: Desc: ExtWarehouseID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtWarehouses_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, ExtWarehouseID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtWarehouse item
   Description: Call UpdateExt to delete ExtWarehouse item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtWarehouse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param ExtWarehouseID: Desc: ExtWarehouseID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtWarehouses(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanyAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyAttches_Company_ExtSystemID_ExtCompanyID_DrawingSeq(Company, ExtSystemID, ExtCompanyID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyAttch item
   Description: Calls GetByID to retrieve the ExtCompanyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanyAttches_Company_ExtSystemID_ExtCompanyID_DrawingSeq(Company, ExtSystemID, ExtCompanyID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompanyAttch for the service
   Description: Calls UpdateExt to update ExtCompanyAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanyAttches_Company_ExtSystemID_ExtCompanyID_DrawingSeq(Company, ExtSystemID, ExtCompanyID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompanyAttch item
   Description: Call UpdateExt to delete ExtCompanyAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyAttches(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerDefs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerDefs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanyTriggerDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerDef item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompanyTriggerDef for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompanyTriggerDef item
   Description: Call UpdateExt to delete ExtCompanyTriggerDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_ExtCompanyTriggerConditionGrps(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtCompanyTriggerConditionGrps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtCompanyTriggerConditionGrps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")/ExtCompanyTriggerConditionGrps",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerDefs_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_ExtCompanyTriggerConditionGrps_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerActionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerActionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerConditionGrp item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerConditionGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerConditionGrp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerActionNum: Desc: TriggerActionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerDefs(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + ")/ExtCompanyTriggerConditionGrps(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerConditionGrps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerConditionGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerConditionGrps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanyTriggerConditionGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerConditionGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerConditionGrps_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerActionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerActionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerConditionGrp item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerConditionGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerConditionGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerActionNum: Desc: TriggerActionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanyTriggerConditionGrps_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerActionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerActionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompanyTriggerConditionGrp for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerConditionGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerConditionGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerActionNum: Desc: TriggerActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerActionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanyTriggerConditionGrps_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerActionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerActionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompanyTriggerConditionGrp item
   Description: Call UpdateExt to delete ExtCompanyTriggerConditionGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerConditionGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerActionNum: Desc: TriggerActionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionGrps(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerActions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerActions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanyTriggerActions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerActions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerActionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerActionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerAction item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerActionNum: Desc: TriggerActionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanyTriggerActions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerActionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerActionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompanyTriggerAction for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerActionNum: Desc: TriggerActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerActionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanyTriggerActions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerActionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerActionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompanyTriggerAction item
   Description: Call UpdateExt to delete ExtCompanyTriggerAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerActionNum: Desc: TriggerActionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerActions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerConditions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerConditions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerConditions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerConditionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanyTriggerConditions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerConditions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerConditions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerConditionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerCondition item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerCondition item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerCondition
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerConditionNum: Desc: TriggerConditionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanyTriggerConditions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerConditionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompanyTriggerCondition for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerCondition. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerCondition
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerConditionNum: Desc: TriggerConditionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanyTriggerConditions_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerConditionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompanyTriggerCondition item
   Description: Call UpdateExt to delete ExtCompanyTriggerCondition item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerCondition
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerConditionNum: Desc: TriggerConditionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditions(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerConditionDatas(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtCompanyTriggerConditionDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtCompanyTriggerConditionDatas
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyTriggerConditionDataRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas",headers=creds) as resp:
           return await resp.json()

async def post_ExtCompanyTriggerConditionDatas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtCompanyTriggerConditionDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionDataRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionDataRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtCompanyTriggerConditionDatas_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum_TriggerConditionDataNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerConditionNum, TriggerConditionDataNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtCompanyTriggerConditionData item
   Description: Calls GetByID to retrieve the ExtCompanyTriggerConditionData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtCompanyTriggerConditionData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerConditionNum: Desc: TriggerConditionNum   Required: True
      :param TriggerConditionDataNum: Desc: TriggerConditionDataNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionDataRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + "," + TriggerConditionDataNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtCompanyTriggerConditionDatas_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum_TriggerConditionDataNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerConditionNum, TriggerConditionDataNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtCompanyTriggerConditionData for the service
   Description: Calls UpdateExt to update ExtCompanyTriggerConditionData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtCompanyTriggerConditionData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerConditionNum: Desc: TriggerConditionNum   Required: True
      :param TriggerConditionDataNum: Desc: TriggerConditionDataNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtCompanyTriggerConditionDataRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + "," + TriggerConditionDataNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtCompanyTriggerConditionDatas_Company_ExtSystemID_ExtCompanyID_SchemaName_DBTableName_TriggerType_TriggerConditionGroupNum_TriggerConditionNum_TriggerConditionDataNum(Company, ExtSystemID, ExtCompanyID, SchemaName, DBTableName, TriggerType, TriggerConditionGroupNum, TriggerConditionNum, TriggerConditionDataNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtCompanyTriggerConditionData item
   Description: Call UpdateExt to delete ExtCompanyTriggerConditionData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtCompanyTriggerConditionData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param DBTableName: Desc: DBTableName   Required: True   Allow empty value : True
      :param TriggerType: Desc: TriggerType   Required: True   Allow empty value : True
      :param TriggerConditionGroupNum: Desc: TriggerConditionGroupNum   Required: True
      :param TriggerConditionNum: Desc: TriggerConditionNum   Required: True
      :param TriggerConditionDataNum: Desc: TriggerConditionDataNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/ExtCompanyTriggerConditionDatas(" + Company + "," + ExtSystemID + "," + ExtCompanyID + "," + SchemaName + "," + DBTableName + "," + TriggerType + "," + TriggerConditionGroupNum + "," + TriggerConditionNum + "," + TriggerConditionDataNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtCompanyListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseExtCompany, whereClauseExtCompanyAttch, whereClauseExtCompanyECC, whereClauseECCDocType, whereClauseECCReportDefaultStyle, whereClauseExtPlant, whereClauseExtWarehouse, whereClauseEntityGLC, whereClauseExtCompanyTriggerDef, whereClauseExtCompanyTriggerConditionGrp, whereClauseExtCompanyTriggerAction, whereClauseExtCompanyTriggerCondition, whereClauseExtCompanyTriggerConditionData, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseExtCompany=" + whereClauseExtCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtCompanyAttch=" + whereClauseExtCompanyAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtCompanyECC=" + whereClauseExtCompanyECC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECCDocType=" + whereClauseECCDocType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECCReportDefaultStyle=" + whereClauseECCReportDefaultStyle
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtPlant=" + whereClauseExtPlant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtWarehouse=" + whereClauseExtWarehouse
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtCompanyTriggerDef=" + whereClauseExtCompanyTriggerDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtCompanyTriggerConditionGrp=" + whereClauseExtCompanyTriggerConditionGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtCompanyTriggerAction=" + whereClauseExtCompanyTriggerAction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtCompanyTriggerCondition=" + whereClauseExtCompanyTriggerCondition
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtCompanyTriggerConditionData=" + whereClauseExtCompanyTriggerConditionData
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extSystemID, extCompanyID, epicorHeaders = None):
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
   params += "extSystemID=" + extSystemID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "extCompanyID=" + extCompanyID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: To return the CodeDescriptionList values of a given table.field.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetECCReportServiceDescList(epicorHeaders = None):
   """  
   Summary: Invoke method GetECCReportServiceDescList
   Description: Method to call to get a Code Description list.
   OperationID: GetECCReportServiceDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetECCReportServiceDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ConvertToMultiCompanyDirect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertToMultiCompanyDirect
   Description: Convert this ExtCompany record from Sonic to Direct
   OperationID: ConvertToMultiCompanyDirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToMultiCompanyDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToMultiCompanyDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertToMultiCompanyServiceBus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertToMultiCompanyServiceBus
   Description: Convert this ExtCompany record from Direct to Sonic
   OperationID: ConvertToMultiCompanyServiceBus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToMultiCompanyServiceBus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToMultiCompanyServiceBus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateXSDSchemas(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateXSDSchemas
   Description: CreateXSDSchemas
   OperationID: CreateXSDSchemas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateXSDSchemas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateXSDSchemas_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WriteXSDSchemasToServer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WriteXSDSchemasToServer
   Description: Write schema files to the proposed location on the server
   OperationID: WriteXSDSchemasToServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteXSDSchemasToServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteXSDSchemasToServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomerConnect(epicorHeaders = None):
   """  
   Summary: Invoke method CustomerConnect
   Description: Customer Connect
   OperationID: CustomerConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomerConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_EntPrsConf(epicorHeaders = None):
   """  
   Summary: Invoke method EntPrsConf
   Description: Enterprise Configurator
   OperationID: EntPrsConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EntPrsConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangedReportService(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedReportService
   Description: This method populate Report list when Report. AutoProgram Changed
   OperationID: ChangedReportService
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedReportService_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedReportService_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateReportService(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateReportService
   Description: This method validate Report Service make sure that it's unique
   OperationID: ValidateReportService
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateReportService_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReportService_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedReportID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedReportID
   Description: This method populate Report Style list when Report ID Changed
   OperationID: ChangedReportID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedStyleNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedStyleNum
   OperationID: ChangedStyleNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedStyleNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedStyleNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ECCAttachmentAccessRisk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ECCAttachmentAccessRisk
   Description: Method to establish if the attachment configuration is a risk for ECC
If the Attachment Type or Document Type records have a client based transfer a warning will be given if selected.
   OperationID: ECCAttachmentAccessRisk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ECCAttachmentAccessRisk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ECCAttachmentAccessRisk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FSA(epicorHeaders = None):
   """  
   Summary: Invoke method FSA
   Description: FSA
   OperationID: FSA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/FSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_Generic(epicorHeaders = None):
   """  
   Summary: Invoke method Generic
   Description: Generic
   OperationID: Generic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Generic_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_InitEntprsConf(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitEntprsConf
   Description: This method initializes/sends the enterprise configurator records for the
specified ExtCompanyID
   OperationID: InitEntprsConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitEntprsConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitEntprsConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitMultiCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitMultiCompany
   Description: This method initializes/sends the applicable GL data for the specified ExtCompanyID
   OperationID: InitMultiCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitMultiCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitMultiCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitCOA
   Description: This method initializes/sends the applicable COA/GL data for the specified ExtCompanyID
   OperationID: InitCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitConsolidationMonitor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitConsolidationMonitor
   Description: This method Initialize/Send Consolidation data for the specified ExtCompanyID
   OperationID: InitConsolidationMonitor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitConsolidationMonitor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitConsolidationMonitor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Mobile(epicorHeaders = None):
   """  
   Summary: Invoke method Mobile
   Description: Mobile
   OperationID: Mobile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Mobile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_MultiCompany(epicorHeaders = None):
   """  
   Summary: Invoke method MultiCompany
   Description: Multi Company
   OperationID: MultiCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MultiCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeECCSiteName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeECCSiteName
   Description: Validate if existing ECCExtended records exist.
The ECCExtended record holds information on the originating site use for creating Order, Quotes, RMAs.
   OperationID: OnChangeECCSiteName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeECCSiteName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeECCSiteName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLocation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLocation
   Description: OnChangeLocation
   OperationID: OnChangeLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTriggerDefTableName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTriggerDefTableName
   Description: OnChangeTriggerDefTableName
   OperationID: OnChangeTriggerDefTableName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTriggerDefTableName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTriggerDefTableName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PLM(epicorHeaders = None):
   """  
   Summary: Invoke method PLM
   Description: PLM
   OperationID: PLM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PLM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SupplierConnect(epicorHeaders = None):
   """  
   Summary: Invoke method SupplierConnect
   Description: Supplier Connect
   OperationID: SupplierConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SupplierConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_TestConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestConnection
   Description: Test Connection
   OperationID: TestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestECCConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestECCConnection
   Description: Test ECC Conneciont
   OperationID: TestECCConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestECCConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestECCConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompanyAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompanyAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompanyECC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompanyECC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyECC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyECC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyECC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECCDocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECCDocType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECCDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECCDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECCDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECCReportDefaultStyle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECCReportDefaultStyle
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECCReportDefaultStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECCReportDefaultStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECCReportDefaultStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtPlant
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtWarehouse
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompanyTriggerDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompanyTriggerDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompanyTriggerConditionGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompanyTriggerConditionGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerConditionGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerConditionGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerConditionGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompanyTriggerAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompanyTriggerAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompanyTriggerCondition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompanyTriggerCondition
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerCondition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerCondition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerCondition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtCompanyTriggerConditionData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtCompanyTriggerConditionData
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtCompanyTriggerConditionData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtCompanyTriggerConditionData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtCompanyTriggerConditionData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCDocTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECCDocTypeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCReportDefaultStyleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECCReportDefaultStyleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyECCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyECCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerActionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyTriggerActionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionDataRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyTriggerConditionDataRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyTriggerConditionGrpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerConditionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyTriggerConditionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtCompanyTriggerDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtCompanyTriggerDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPlantRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPlantRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtWarehouseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtWarehouseRow] = obj["value"]
      pass

class Erp_Tablesets_ECCDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with.  """  
      self.ECCID:int = obj["ECCID"]
      """  Unique ID.  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """  Unique identifier of a DocType.  By selecting this Doc Type all related attachments will be viewable on the web.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DocTypeDescription:str = obj["DocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECCReportDefaultStyleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with.  """  
      self.ECCID:int = obj["ECCID"]
      """  Unique ID.  """  
      self.AutoProgram:str = obj["AutoProgram"]
      """  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StyleList:str = obj["StyleList"]
      self.RptDescription:str = obj["RptDescription"]
      self.StyleDescription:str = obj["StyleDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ExtSystemID:str = obj["ExtSystemID"]
      self.ExtCompanyID:str = obj["ExtCompanyID"]
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

class Erp_Tablesets_ExtCompanyECCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with.  """  
      self.ECCID:int = obj["ECCID"]
      """  Unique ID.  """  
      self.ECCURL:str = obj["ECCURL"]
      """  URL for ECC uploads  """  
      self.ECCPassword:str = obj["ECCPassword"]
      """  ECC Password  """  
      self.DefaultEpicorUserID:str = obj["DefaultEpicorUserID"]
      """  User ID  """  
      self.DefaultEpicorCustNum:int = obj["DefaultEpicorCustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.DefaultMiscChargeCode:str = obj["DefaultMiscChargeCode"]
      """  Miscellaneous charge code for ECC shipping charges  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultDiscountCode:str = obj["DefaultDiscountCode"]
      """  Miscellaneous charge code for ECC discount  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link To Task set  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """  Inbound attachments from the web will be related to this Doc Type.  """  
      self.CNCPrefix:str = obj["CNCPrefix"]
      """  Customer ID prefix that all new customers created by the CNC message will begin with, followed by an incremented number.  """  
      self.CNCSeq:int = obj["CNCSeq"]
      """  Incremented sequence that will be added to the prefix to create unique Customer IDs for all new customers created from CNC message.  """  
      self.TimeOutLimit:int = obj["TimeOutLimit"]
      """  Specifies the length of time, in seconds, that the sync waits for a response from ECC web site.  """  
      self.RecycleLimit:int = obj["RecycleLimit"]
      """  Specifies the number of times the sync will attempt to reprocess a previous failed sync.  """  
      self.UseLocation:bool = obj["UseLocation"]
      """  Use Location or use the standard Brand Site.  """  
      self.ECCSiteName:str = obj["ECCSiteName"]
      """  ECC Site Name, needs to match what is setup in ECC.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  Link to Work Flow Group  """  
      self.BTCashGrpPfx:str = obj["BTCashGrpPfx"]
      """  Specifies the cash group prefix for ECC payments. All of the ECC payment cash groups are grouped together using this user-defined prefix.  """  
      self.BTDefBankAcctID:str = obj["BTDefBankAcctID"]
      """  Select the default bank to be used for ECC payments from the list of available banks.  """  
      self.ViewDefaultDoc:bool = obj["ViewDefaultDoc"]
      """  Select this checkbox to indicate Default Documents will be viewable on the web.  Only Default Documents of type File System Document will be supported.  """  
      self.InvcGrpPfx:str = obj["InvcGrpPfx"]
      """  Specifies the A/R invoice group prefix for all ECC payments. All of the ECC payment invoices are grouped together, separate from other shipments using this user-defined prefix.  """  
      self.SendPartAttribute:bool = obj["SendPartAttribute"]
      """  Select this option to send populated part attributes to ECC  """  
      self.EnableDefDocsViewable:bool = obj["EnableDefDocsViewable"]
      """  True when company Allow default document is enabled and the method is File System.  """  
      self.ECCPasswordMasked:str = obj["ECCPasswordMasked"]
      """  ECC Masked password field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.DiscountCodeDescription:str = obj["DiscountCodeDescription"]
      self.DocTypeDescription:str = obj["DocTypeDescription"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.UserIDName:str = obj["UserIDName"]
      self.WFGroupIDDescription:str = obj["WFGroupIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.SendCustomer:bool = obj["SendCustomer"]
      """  Customers will be sent . CustomerType = "CUS". Init YES  """  
      self.SendProspect:bool = obj["SendProspect"]
      """  Prospects will be sent . CustomerType = "PRO". Init YES  """  
      self.SendSuspect:bool = obj["SendSuspect"]
      """  Suspects  will be sent. CustomerType = "SUS". Init NO  """  
      self.SendVend:bool = obj["SendVend"]
      """  Vendors will be sent .  Init YES  """  
      self.SendPart:bool = obj["SendPart"]
      """  Parts will be sent.  Init NO (Future USE)  """  
      self.SendShip:bool = obj["SendShip"]
      """  Shipments will be sent .  Init YES  """  
      self.SendARInv:bool = obj["SendARInv"]
      """  AR Invoices will be sent .  Init YES  """  
      self.RcvARInv:bool = obj["RcvARInv"]
      """  AR Invoices will be received .  Init YES  """  
      self.SendAPInv:bool = obj["SendAPInv"]
      """  AP Invoices will be sent .  Init YES  """  
      self.RcvAPInv:bool = obj["RcvAPInv"]
      """  AP Invoices will be received .  Init YES  """  
      self.APPurchType:bool = obj["APPurchType"]
      """  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  """  
      self.SendAckToQue:bool = obj["SendAckToQue"]
      """  For this interface, should acknowledgments be sent back to the interfaced software when a record is received into the intermediate tables?  """  
      self.ICTrading:bool = obj["ICTrading"]
      """  Indicates if this external company setup supports Inter-Company Trading.  """  
      self.ICVendorNum:int = obj["ICVendorNum"]
      """  A  unique integer assigned by the system to identify the Vendor participating in the Inter-Company Trading.  """  
      self.ICCustNum:int = obj["ICCustNum"]
      """  A  unique integer assigned by the system to identify the Customer participating in the Inter-Company Trading.  """  
      self.ExtCustID:str = obj["ExtCustID"]
      """  A user defined external customer ID.  Identifies the External Customer participating in the Inter-Company Trading.  """  
      self.ExtVendorID:str = obj["ExtVendorID"]
      """  A user defined external vendor ID.  Identifies the External Vendor participating in the Inter-Company Trading.  """  
      self.APDiscount:bool = obj["APDiscount"]
      """  Indicates that the discount amount by line needs to be captured to be sent to the Financials package  """  
      self.AuxPrgmType:str = obj["AuxPrgmType"]
      """  The type of program being called (ProgressProgram or WindowsProgram)  """  
      self.AuxPrgmName:str = obj["AuxPrgmName"]
      """  Name of Auxiliary program to run to alert external system that there are records ready for processing  """  
      self.SendPOSugg:bool = obj["SendPOSugg"]
      """  New PO Suggestions will be sent.  """  
      self.TransferDays:int = obj["TransferDays"]
      """  Number of days it will take to transfer an order from one company to the other.  Only for Inter-Company traders.  Will subtract this number from the po need by date to get the correct need by date on the order side.  Controlled on the Order side (po due-date - transfertime = orderdate)  """  
      self.PONumBlockSize:int = obj["PONumBlockSize"]
      """  Size of blocks for POHeader.PONum to be generated for this Consolidated Purchasing Company.  """  
      self.PONumBlockReorderPoint:int = obj["PONumBlockReorderPoint"]
      """  When a Consolidated Purchasing Company requests a new block because their portion of their POHeader.PONum block is less than this Reorder Point, create a new block and send it out.  """  
      self.PONumBlockWarnPoint:int = obj["PONumBlockWarnPoint"]
      """  When a Consolidated Purchasing Company creates a Purchase Order and the number of allocated PONum values drops below this warning point, message the user to inform them.  """  
      self.DefaultPlant:str = obj["DefaultPlant"]
      """  Establishes the default ExtSite.ExtSiteID to be used as the default for a Site field during creation of a Consolidated Purchase Order Release.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SendGLAccounts:bool = obj["SendGLAccounts"]
      """  Send G/L Accounts for Multi-Company Journal.  """  
      self.AllowGJAlloc:bool = obj["AllowGJAlloc"]
      """  Indicates if the current company is allowed to send Multi-Company General Journals to this external company.  """  
      self.AllowAPAlloc:bool = obj["AllowAPAlloc"]
      """  Indicates if the current company is allowed to send Multi-Company AP G/L entries to this external company.  """  
      self.JrnGroupPrefix:str = obj["JrnGroupPrefix"]
      """  The Journal Group prefix to use when determining the group ID for the Multi-Company Journals coming from this external company.  """  
      self.AutoPostGJ:bool = obj["AutoPostGJ"]
      """  Flag to indicate if the Multi-Company Journals coming from this external company needs to be posted automatically.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The Journal Code to use to enter Multi-Company Journals from this external company.  """  
      self.CPayGroupPrefix:str = obj["CPayGroupPrefix"]
      """  The default Invoice Group Prefix that will be used by Centralized Payment process.  """  
      self.CPayAutoPost:bool = obj["CPayAutoPost"]
      """  The flag to indicate if invoices flagged for Centralized Payment from external company will be posted automatically.  """  
      self.CPayLegalNum:str = obj["CPayLegalNum"]
      """   This field will indicate how Legal Number will be generated.  The valid options are:
'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 
'N'  -  Generate New Legal Number using the current company's Legal Number rules.  """  
      self.AutoLoadCust:bool = obj["AutoLoadCust"]
      """  When receiving global customers, try to create/link the Part without human intervention  """  
      self.AutoLoadVend:bool = obj["AutoLoadVend"]
      """  When receiving global vendors, try to create/link a vendor without human intervention  """  
      self.AutoLoadPart:bool = obj["AutoLoadPart"]
      """  When receiving Global Parts, try to create/link a Part without human intervention  """  
      self.SendRev:bool = obj["SendRev"]
      """  Part revisions will be sent.  Init NO (Future USE)  """  
      self.SendPerCon:bool = obj["SendPerCon"]
      """  PerCon will be sent.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowAPPurchType:bool = obj["AllowAPPurchType"]
      self.EnableCPayGroup:bool = obj["EnableCPayGroup"]
      """  Flag to indicate when to enable the CPay Group Prefix.  """  
      self.EnableCPayLegal:bool = obj["EnableCPayLegal"]
      """  Flag to indicate when to enable the CPay Legal Number combo  """  
      self.DispCPayParent:bool = obj["DispCPayParent"]
      """  Flag to indicate if the External Company is the Central Payment Parent Company.  """  
      self.EnableARIntercompany:bool = obj["EnableARIntercompany"]
      """  Flag to indicate when to enable the AR Intercompany Account button.  """  
      self.ExtSystemExtSystemName:str = obj["ExtSystemExtSystemName"]
      """  Full Name of external package  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.LinkCustomerBTName:str = obj["LinkCustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.LinkCustomerCustID:str = obj["LinkCustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.LinkCustomerName:str = obj["LinkCustomerName"]
      """  The full name of the customer.  """  
      self.LinkVendorAddress1:str = obj["LinkVendorAddress1"]
      """  First address line of the Supplier  """  
      self.LinkVendorCity:str = obj["LinkVendorCity"]
      """  City portion of the address of the Supplier  """  
      self.LinkVendorDefaultFOB:str = obj["LinkVendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.LinkVendorTermsCode:str = obj["LinkVendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.LinkVendorAddress2:str = obj["LinkVendorAddress2"]
      """  Second address line of the Supplier  """  
      self.LinkVendorCountry:str = obj["LinkVendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.LinkVendorName:str = obj["LinkVendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.LinkVendorVendorID:str = obj["LinkVendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.LinkVendorAddress3:str = obj["LinkVendorAddress3"]
      """  Third address line of the Supplier  """  
      self.LinkVendorCurrencyCode:str = obj["LinkVendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LinkVendorState:str = obj["LinkVendorState"]
      """  Can be blank.  """  
      self.LinkVendorZIP:str = obj["LinkVendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.CompanyCountryLangNameID:str = obj["CompanyCountryLangNameID"]
      """  CompanyCountryLangNameID  """  
      self.SendCustomer:bool = obj["SendCustomer"]
      """  Customers will be sent . CustomerType = "CUS". Init YES  """  
      self.SendProspect:bool = obj["SendProspect"]
      """  Prospects will be sent . CustomerType = "PRO". Init YES  """  
      self.SendSuspect:bool = obj["SendSuspect"]
      """  Suspects  will be sent. CustomerType = "SUS". Init NO  """  
      self.SendVend:bool = obj["SendVend"]
      """  Vendors will be sent .  Init YES  """  
      self.SendPart:bool = obj["SendPart"]
      """  Parts will be sent.  Init NO (Future USE)  """  
      self.SendShip:bool = obj["SendShip"]
      """  Shipments will be sent .  Init YES  """  
      self.SendARInv:bool = obj["SendARInv"]
      """  AR Invoices will be sent .  Init YES  """  
      self.RcvARInv:bool = obj["RcvARInv"]
      """  AR Invoices will be received .  Init YES  """  
      self.SendAPInv:bool = obj["SendAPInv"]
      """  AP Invoices will be sent .  Init YES  """  
      self.RcvAPInv:bool = obj["RcvAPInv"]
      """  AP Invoices will be received .  Init YES  """  
      self.APPurchType:bool = obj["APPurchType"]
      """  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  """  
      self.SendAckToQue:bool = obj["SendAckToQue"]
      """  For this interface, should acknowledgments be sent back to the interfaced software when a record is received into the intermediate tables?  """  
      self.ICTrading:bool = obj["ICTrading"]
      """  Indicates if this external company setup supports Inter-Company Trading.  """  
      self.ICVendorNum:int = obj["ICVendorNum"]
      """  A  unique integer assigned by the system to identify the Vendor participating in the Inter-Company Trading.  """  
      self.ICCustNum:int = obj["ICCustNum"]
      """  A  unique integer assigned by the system to identify the Customer participating in the Inter-Company Trading.  """  
      self.ExtCustID:str = obj["ExtCustID"]
      """  A user defined external customer ID.  Identifies the External Customer participating in the Inter-Company Trading.  """  
      self.ExtVendorID:str = obj["ExtVendorID"]
      """  A user defined external vendor ID.  Identifies the External Vendor participating in the Inter-Company Trading.  """  
      self.APDiscount:bool = obj["APDiscount"]
      """  Indicates that the discount amount by line needs to be captured to be sent to the Financials package  """  
      self.AuxPrgmType:str = obj["AuxPrgmType"]
      """  The type of program being called (ProgressProgram or WindowsProgram)  """  
      self.AuxPrgmName:str = obj["AuxPrgmName"]
      """  Name of Auxiliary program to run to alert external system that there are records ready for processing  """  
      self.SendPOSugg:bool = obj["SendPOSugg"]
      """  New PO Suggestions will be sent.  """  
      self.LastConDate:str = obj["LastConDate"]
      """  Last date the connection was made successfully  """  
      self.LastConTime:int = obj["LastConTime"]
      """  Last Time the connection was made successfully  """  
      self.LastFailedDate:str = obj["LastFailedDate"]
      """  last date the connection was attempted and failed  """  
      self.LastFailedTime:int = obj["LastFailedTime"]
      """  Last time the connection was tried and failed  """  
      self.TransferDays:int = obj["TransferDays"]
      """  Number of days it will take to transfer an order from one company to the other.  Only for Inter-Company traders.  Will subtract this number from the po need by date to get the correct need by date on the order side.  Controlled on the Order side (po due-date - transfertime = orderdate)  """  
      self.PONumBlockSize:int = obj["PONumBlockSize"]
      """  Size of blocks for POHeader.PONum to be generated for this Consolidated Purchasing Company.  """  
      self.PONumBlockReorderPoint:int = obj["PONumBlockReorderPoint"]
      """  When a Consolidated Purchasing Company requests a new block because their portion of their POHeader.PONum block is less than this Reorder Point, create a new block and send it out.  """  
      self.PONumBlockWarnPoint:int = obj["PONumBlockWarnPoint"]
      """  When a Consolidated Purchasing Company creates a Purchase Order and the number of allocated PONum values drops below this warning point, message the user to inform them.  """  
      self.DefaultPlant:str = obj["DefaultPlant"]
      """  Establishes the default ExtSite.ExtSiteID to be used as the default for a Site field during creation of a Consolidated Purchase Order Release.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SendGLAccounts:bool = obj["SendGLAccounts"]
      """  Send G/L Accounts for Multi-Company Journal.  """  
      self.AllowGJAlloc:bool = obj["AllowGJAlloc"]
      """  Indicates if the current company is allowed to send Multi-Company General Journals to this external company.  """  
      self.AllowAPAlloc:bool = obj["AllowAPAlloc"]
      """  Indicates if the current company is allowed to send Multi-Company AP G/L entries to this external company.  """  
      self.JrnGroupPrefix:str = obj["JrnGroupPrefix"]
      """  The Journal Group prefix to use when determining the group ID for the Multi-Company Journals coming from this external company.  """  
      self.AutoPostGJ:bool = obj["AutoPostGJ"]
      """  Flag to indicate if the Multi-Company Journals coming from this external company needs to be posted automatically.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The Journal Code to use to enter Multi-Company Journals from this external company.  """  
      self.CPayGroupPrefix:str = obj["CPayGroupPrefix"]
      """  The default Invoice Group Prefix that will be used by Centralized Payment process.  """  
      self.CPayAutoPost:bool = obj["CPayAutoPost"]
      """  The flag to indicate if invoices flagged for Centralized Payment from external company will be posted automatically.  """  
      self.CPayLegalNum:str = obj["CPayLegalNum"]
      """   This field will indicate how Legal Number will be generated.  The valid options are:
'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 
'N'  -  Generate New Legal Number using the current company's Legal Number rules.  """  
      self.AutoLoadCust:bool = obj["AutoLoadCust"]
      """  When receiving global customers, try to create/link the Part without human intervention  """  
      self.AutoLoadVend:bool = obj["AutoLoadVend"]
      """  When receiving global vendors, try to create/link a vendor without human intervention  """  
      self.AutoLoadPart:bool = obj["AutoLoadPart"]
      """  When receiving Global Parts, try to create/link a Part without human intervention  """  
      self.SendRev:bool = obj["SendRev"]
      """  Part revisions will be sent.  Init NO (Future USE)  """  
      self.SendPerCon:bool = obj["SendPerCon"]
      """  PerCon will be sent.  """  
      self.MCSegOnly:bool = obj["MCSegOnly"]
      """  MCSegOnly  """  
      self.SendConfigurator:bool = obj["SendConfigurator"]
      """  SendConfigurator  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendGlobalCOA:bool = obj["SendGlobalCOA"]
      """  Turns Global COA on  """  
      self.SendGlobalCOAType:str = obj["SendGlobalCOAType"]
      """  Indicates how much of the COA supporting structure to send. seg`Send Segments Only~coa`Send Full COA  """  
      self.AlwaysUseGLInterComp:bool = obj["AlwaysUseGLInterComp"]
      """  It is used for rules of creation offsetting GL inter-company lines in multi-company process. If it is checked the journal will have an offsetting line with inter-company account for each multi-company line.  """  
      self.CColGroupPrefix:str = obj["CColGroupPrefix"]
      """  The default Invoice Group Prefix that will be used by Centralized Collection process.  """  
      self.CColCPayLegalNum:str = obj["CColCPayLegalNum"]
      """  This field will indicate how Legal Number will be generated for Central Collection invoices.  The valid options are: 'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 'N'  -  Generate New Legal Number using the current company's Legal Number rules.  """  
      self.SendDynAttr:bool = obj["SendDynAttr"]
      """  Dynamic Attributes will be sent.  Init NO  """  
      self.RcvDynAttr:bool = obj["RcvDynAttr"]
      """  Dynamic Attributes will be received.  Init NO  """  
      self.DispCPayParent:bool = obj["DispCPayParent"]
      """  Flag to indicate if the External Company is the Central Payment Parent Company.  """  
      self.EnableARIntercompany:bool = obj["EnableARIntercompany"]
      """  Flag to indicate when to enable the AR Intercompany Account button.  """  
      self.EnableConvertToDirect:bool = obj["EnableConvertToDirect"]
      self.EnableConvertToSonic:bool = obj["EnableConvertToSonic"]
      self.EnableCPayGroup:bool = obj["EnableCPayGroup"]
      """  Flag to indicate when to enable the CPay Group Prefix.  """  
      self.EnableCPayLegal:bool = obj["EnableCPayLegal"]
      """  Flag to indicate when to enable the CPay Legal Number combo  """  
      self.ExtCompanyName:str = obj["ExtCompanyName"]
      """  Name or description of the external company.  """  
      self.ExtSystemIDTransferMethod:str = obj["ExtSystemIDTransferMethod"]
      self.AllowAPPurchType:bool = obj["AllowAPPurchType"]
      self.EnableCColCPayLegalNum:bool = obj["EnableCColCPayLegalNum"]
      """  Flag to indicate when to enable the Central Collection Legal Number  """  
      self.EnableCColGroupPrefix:bool = obj["EnableCColGroupPrefix"]
      """  Flag to indicate when to enable the Central Collection Group Prefix.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ExtSystemExtSystemName:str = obj["ExtSystemExtSystemName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.LinkCustomerName:str = obj["LinkCustomerName"]
      self.LinkCustomerBTName:str = obj["LinkCustomerBTName"]
      self.LinkCustomerCustID:str = obj["LinkCustomerCustID"]
      self.LinkCustomerInactive:bool = obj["LinkCustomerInactive"]
      self.LinkVendorAddress1:str = obj["LinkVendorAddress1"]
      self.LinkVendorCity:str = obj["LinkVendorCity"]
      self.LinkVendorDefaultFOB:str = obj["LinkVendorDefaultFOB"]
      self.LinkVendorTermsCode:str = obj["LinkVendorTermsCode"]
      self.LinkVendorAddress2:str = obj["LinkVendorAddress2"]
      self.LinkVendorCountry:str = obj["LinkVendorCountry"]
      self.LinkVendorName:str = obj["LinkVendorName"]
      self.LinkVendorVendorID:str = obj["LinkVendorVendorID"]
      self.LinkVendorAddress3:str = obj["LinkVendorAddress3"]
      self.LinkVendorCurrencyCode:str = obj["LinkVendorCurrencyCode"]
      self.LinkVendorState:str = obj["LinkVendorState"]
      self.LinkVendorZIP:str = obj["LinkVendorZIP"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.TriggerActionNum:int = obj["TriggerActionNum"]
      """  TriggerActionNum  """  
      self.ActionType:str = obj["ActionType"]
      """  ActionType  """  
      self.WorkflowName:str = obj["WorkflowName"]
      """  WorkflowName  """  
      self.ActionIsAsynchronous:bool = obj["ActionIsAsynchronous"]
      """  ActionIsAsynchronous  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerConditionDataRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.TriggerConditionGroupNum:int = obj["TriggerConditionGroupNum"]
      """  TriggerConditionGroupNum  """  
      self.TriggerConditionNum:int = obj["TriggerConditionNum"]
      """  TriggerConditionNum  """  
      self.TriggerConditionDataNum:int = obj["TriggerConditionDataNum"]
      """  TriggerConditionDataNum  """  
      self.Data:str = obj["Data"]
      """  Data  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerConditionGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.TriggerConditionGroupNum:int = obj["TriggerConditionGroupNum"]
      """  TriggerConditionGroupNum  """  
      self.TriggerActionNum:int = obj["TriggerActionNum"]
      """  TriggerActionNum  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerConditionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.TriggerConditionGroupNum:int = obj["TriggerConditionGroupNum"]
      """  TriggerConditionGroupNum  """  
      self.TriggerConditionNum:int = obj["TriggerConditionNum"]
      """  TriggerConditionNum  """  
      self.OrderSeq:int = obj["OrderSeq"]
      """  OrderSeq  """  
      self.Operator:str = obj["Operator"]
      """  Operator  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.ConditionTypeName:str = obj["ConditionTypeName"]
      """  ConditionTypeName  """  
      self.Postfix:str = obj["Postfix"]
      """  Postfix  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.Data:str = obj["Data"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.IsEnabled:bool = obj["IsEnabled"]
      """  IsEnabled  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DeveloperMode:bool = obj["DeveloperMode"]
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtPlantID:str = obj["ExtPlantID"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Main phone number of the Site.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Main fax number of the Site.  """  
      self.DefaultWhse:str = obj["DefaultWhse"]
      """  ExtWarehouse.ExtWarehouseID as the default external warehouse for this external Site.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtWarehouseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtPlantID:str = obj["ExtPlantID"]
      """  Unique identifier of this external Site assigned by the user.  """  
      self.ExtWarehouseID:str = obj["ExtWarehouseID"]
      """  Unique identifier of this warehouse assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangedReportID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

class ChangedReportID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedReportService_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

class ChangedReportService_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedStyleNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

class ChangedStyleNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConvertToMultiCompanyDirect_input:
   """ Required : 
   ipCompany
   ipExtSystemID
   ipTransferMethod
   ipExtCompanyID
   ipSysRowID
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      """  Input the ExtCompany.Company value to be converted  """  
      self.ipExtSystemID:str = obj["ipExtSystemID"]
      """  Input the ExtCompany.ExtSystemID value to be converted  """  
      self.ipTransferMethod:str = obj["ipTransferMethod"]
      """  Input the ExtCompany.TransferMethod value to be converted  """  
      self.ipExtCompanyID:str = obj["ipExtCompanyID"]
      """  Input the ExtCompany.ExtCompanyID value to be converted  """  
      self.ipSysRowID:str = obj["ipSysRowID"]
      """  Input the ExtCompany.SysRowID value to be converted  """  
      pass

class ConvertToMultiCompanyDirect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opSuccess:bool = obj["opSuccess"]
      pass

      """  output parameters  """  

class ConvertToMultiCompanyServiceBus_input:
   """ Required : 
   ipCompany
   ipExtSystemID
   ipTransferMethod
   ipExtCompanyID
   ipSysRowID
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      """  Input the ExtCompany.Company value to be converted  """  
      self.ipExtSystemID:str = obj["ipExtSystemID"]
      """  Input the ExtCompany.ExtSystemID value to be converted  """  
      self.ipTransferMethod:str = obj["ipTransferMethod"]
      """  Input the ExtCompany.TransferMethod value to be converted  """  
      self.ipExtCompanyID:str = obj["ipExtCompanyID"]
      """  Input the ExtCompany.ExtCompanyID value to be converted  """  
      self.ipSysRowID:str = obj["ipSysRowID"]
      """  Input the ExtCompany.SysRowID value to be converted  """  
      pass

class ConvertToMultiCompanyServiceBus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opSuccess:bool = obj["opSuccess"]
      pass

      """  output parameters  """  

class CreateXSDSchemas_input:
   """ Required : 
   proposedLocation
   proposedTableName
   """  
   def __init__(self, obj):
      self.proposedLocation:str = obj["proposedLocation"]
      self.proposedTableName:str = obj["proposedTableName"]
      pass

class CreateXSDSchemas_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.success:bool = obj["success"]
      pass

      """  output parameters  """  

class CustomerConnect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.disabledList:str = obj["parameters"]
      self.checkedList:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   extSystemID
   extCompanyID
   """  
   def __init__(self, obj):
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class ECCAttachmentAccessRisk_input:
   """ Required : 
   defaultDocsEnabled
   addedDocType
   """  
   def __init__(self, obj):
      self.defaultDocsEnabled:bool = obj["defaultDocsEnabled"]
      """  Will collect default storage type and check for client transfer  """  
      self.addedDocType:str = obj["addedDocType"]
      """  Checks the File Transfer Mode on the Doc Type  """  
      pass

class ECCAttachmentAccessRisk_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class EntPrsConf_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.disabledList:str = obj["parameters"]
      self.checkedList:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ECCDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with.  """  
      self.ECCID:int = obj["ECCID"]
      """  Unique ID.  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """  Unique identifier of a DocType.  By selecting this Doc Type all related attachments will be viewable on the web.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DocTypeDescription:str = obj["DocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECCReportDefaultStyleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with.  """  
      self.ECCID:int = obj["ECCID"]
      """  Unique ID.  """  
      self.AutoProgram:str = obj["AutoProgram"]
      """  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StyleList:str = obj["StyleList"]
      self.RptDescription:str = obj["RptDescription"]
      self.StyleDescription:str = obj["StyleDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ExtSystemID:str = obj["ExtSystemID"]
      self.ExtCompanyID:str = obj["ExtCompanyID"]
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

class Erp_Tablesets_ExtCompanyECCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with.  """  
      self.ECCID:int = obj["ECCID"]
      """  Unique ID.  """  
      self.ECCURL:str = obj["ECCURL"]
      """  URL for ECC uploads  """  
      self.ECCPassword:str = obj["ECCPassword"]
      """  ECC Password  """  
      self.DefaultEpicorUserID:str = obj["DefaultEpicorUserID"]
      """  User ID  """  
      self.DefaultEpicorCustNum:int = obj["DefaultEpicorCustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.DefaultMiscChargeCode:str = obj["DefaultMiscChargeCode"]
      """  Miscellaneous charge code for ECC shipping charges  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultDiscountCode:str = obj["DefaultDiscountCode"]
      """  Miscellaneous charge code for ECC discount  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link To Task set  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """  Inbound attachments from the web will be related to this Doc Type.  """  
      self.CNCPrefix:str = obj["CNCPrefix"]
      """  Customer ID prefix that all new customers created by the CNC message will begin with, followed by an incremented number.  """  
      self.CNCSeq:int = obj["CNCSeq"]
      """  Incremented sequence that will be added to the prefix to create unique Customer IDs for all new customers created from CNC message.  """  
      self.TimeOutLimit:int = obj["TimeOutLimit"]
      """  Specifies the length of time, in seconds, that the sync waits for a response from ECC web site.  """  
      self.RecycleLimit:int = obj["RecycleLimit"]
      """  Specifies the number of times the sync will attempt to reprocess a previous failed sync.  """  
      self.UseLocation:bool = obj["UseLocation"]
      """  Use Location or use the standard Brand Site.  """  
      self.ECCSiteName:str = obj["ECCSiteName"]
      """  ECC Site Name, needs to match what is setup in ECC.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  Link to Work Flow Group  """  
      self.BTCashGrpPfx:str = obj["BTCashGrpPfx"]
      """  Specifies the cash group prefix for ECC payments. All of the ECC payment cash groups are grouped together using this user-defined prefix.  """  
      self.BTDefBankAcctID:str = obj["BTDefBankAcctID"]
      """  Select the default bank to be used for ECC payments from the list of available banks.  """  
      self.ViewDefaultDoc:bool = obj["ViewDefaultDoc"]
      """  Select this checkbox to indicate Default Documents will be viewable on the web.  Only Default Documents of type File System Document will be supported.  """  
      self.InvcGrpPfx:str = obj["InvcGrpPfx"]
      """  Specifies the A/R invoice group prefix for all ECC payments. All of the ECC payment invoices are grouped together, separate from other shipments using this user-defined prefix.  """  
      self.SendPartAttribute:bool = obj["SendPartAttribute"]
      """  Select this option to send populated part attributes to ECC  """  
      self.EnableDefDocsViewable:bool = obj["EnableDefDocsViewable"]
      """  True when company Allow default document is enabled and the method is File System.  """  
      self.ECCPasswordMasked:str = obj["ECCPasswordMasked"]
      """  ECC Masked password field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.DiscountCodeDescription:str = obj["DiscountCodeDescription"]
      self.DocTypeDescription:str = obj["DocTypeDescription"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.UserIDName:str = obj["UserIDName"]
      self.WFGroupIDDescription:str = obj["WFGroupIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.SendCustomer:bool = obj["SendCustomer"]
      """  Customers will be sent . CustomerType = "CUS". Init YES  """  
      self.SendProspect:bool = obj["SendProspect"]
      """  Prospects will be sent . CustomerType = "PRO". Init YES  """  
      self.SendSuspect:bool = obj["SendSuspect"]
      """  Suspects  will be sent. CustomerType = "SUS". Init NO  """  
      self.SendVend:bool = obj["SendVend"]
      """  Vendors will be sent .  Init YES  """  
      self.SendPart:bool = obj["SendPart"]
      """  Parts will be sent.  Init NO (Future USE)  """  
      self.SendShip:bool = obj["SendShip"]
      """  Shipments will be sent .  Init YES  """  
      self.SendARInv:bool = obj["SendARInv"]
      """  AR Invoices will be sent .  Init YES  """  
      self.RcvARInv:bool = obj["RcvARInv"]
      """  AR Invoices will be received .  Init YES  """  
      self.SendAPInv:bool = obj["SendAPInv"]
      """  AP Invoices will be sent .  Init YES  """  
      self.RcvAPInv:bool = obj["RcvAPInv"]
      """  AP Invoices will be received .  Init YES  """  
      self.APPurchType:bool = obj["APPurchType"]
      """  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  """  
      self.SendAckToQue:bool = obj["SendAckToQue"]
      """  For this interface, should acknowledgments be sent back to the interfaced software when a record is received into the intermediate tables?  """  
      self.ICTrading:bool = obj["ICTrading"]
      """  Indicates if this external company setup supports Inter-Company Trading.  """  
      self.ICVendorNum:int = obj["ICVendorNum"]
      """  A  unique integer assigned by the system to identify the Vendor participating in the Inter-Company Trading.  """  
      self.ICCustNum:int = obj["ICCustNum"]
      """  A  unique integer assigned by the system to identify the Customer participating in the Inter-Company Trading.  """  
      self.ExtCustID:str = obj["ExtCustID"]
      """  A user defined external customer ID.  Identifies the External Customer participating in the Inter-Company Trading.  """  
      self.ExtVendorID:str = obj["ExtVendorID"]
      """  A user defined external vendor ID.  Identifies the External Vendor participating in the Inter-Company Trading.  """  
      self.APDiscount:bool = obj["APDiscount"]
      """  Indicates that the discount amount by line needs to be captured to be sent to the Financials package  """  
      self.AuxPrgmType:str = obj["AuxPrgmType"]
      """  The type of program being called (ProgressProgram or WindowsProgram)  """  
      self.AuxPrgmName:str = obj["AuxPrgmName"]
      """  Name of Auxiliary program to run to alert external system that there are records ready for processing  """  
      self.SendPOSugg:bool = obj["SendPOSugg"]
      """  New PO Suggestions will be sent.  """  
      self.TransferDays:int = obj["TransferDays"]
      """  Number of days it will take to transfer an order from one company to the other.  Only for Inter-Company traders.  Will subtract this number from the po need by date to get the correct need by date on the order side.  Controlled on the Order side (po due-date - transfertime = orderdate)  """  
      self.PONumBlockSize:int = obj["PONumBlockSize"]
      """  Size of blocks for POHeader.PONum to be generated for this Consolidated Purchasing Company.  """  
      self.PONumBlockReorderPoint:int = obj["PONumBlockReorderPoint"]
      """  When a Consolidated Purchasing Company requests a new block because their portion of their POHeader.PONum block is less than this Reorder Point, create a new block and send it out.  """  
      self.PONumBlockWarnPoint:int = obj["PONumBlockWarnPoint"]
      """  When a Consolidated Purchasing Company creates a Purchase Order and the number of allocated PONum values drops below this warning point, message the user to inform them.  """  
      self.DefaultPlant:str = obj["DefaultPlant"]
      """  Establishes the default ExtSite.ExtSiteID to be used as the default for a Site field during creation of a Consolidated Purchase Order Release.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SendGLAccounts:bool = obj["SendGLAccounts"]
      """  Send G/L Accounts for Multi-Company Journal.  """  
      self.AllowGJAlloc:bool = obj["AllowGJAlloc"]
      """  Indicates if the current company is allowed to send Multi-Company General Journals to this external company.  """  
      self.AllowAPAlloc:bool = obj["AllowAPAlloc"]
      """  Indicates if the current company is allowed to send Multi-Company AP G/L entries to this external company.  """  
      self.JrnGroupPrefix:str = obj["JrnGroupPrefix"]
      """  The Journal Group prefix to use when determining the group ID for the Multi-Company Journals coming from this external company.  """  
      self.AutoPostGJ:bool = obj["AutoPostGJ"]
      """  Flag to indicate if the Multi-Company Journals coming from this external company needs to be posted automatically.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The Journal Code to use to enter Multi-Company Journals from this external company.  """  
      self.CPayGroupPrefix:str = obj["CPayGroupPrefix"]
      """  The default Invoice Group Prefix that will be used by Centralized Payment process.  """  
      self.CPayAutoPost:bool = obj["CPayAutoPost"]
      """  The flag to indicate if invoices flagged for Centralized Payment from external company will be posted automatically.  """  
      self.CPayLegalNum:str = obj["CPayLegalNum"]
      """   This field will indicate how Legal Number will be generated.  The valid options are:
'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 
'N'  -  Generate New Legal Number using the current company's Legal Number rules.  """  
      self.AutoLoadCust:bool = obj["AutoLoadCust"]
      """  When receiving global customers, try to create/link the Part without human intervention  """  
      self.AutoLoadVend:bool = obj["AutoLoadVend"]
      """  When receiving global vendors, try to create/link a vendor without human intervention  """  
      self.AutoLoadPart:bool = obj["AutoLoadPart"]
      """  When receiving Global Parts, try to create/link a Part without human intervention  """  
      self.SendRev:bool = obj["SendRev"]
      """  Part revisions will be sent.  Init NO (Future USE)  """  
      self.SendPerCon:bool = obj["SendPerCon"]
      """  PerCon will be sent.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowAPPurchType:bool = obj["AllowAPPurchType"]
      self.EnableCPayGroup:bool = obj["EnableCPayGroup"]
      """  Flag to indicate when to enable the CPay Group Prefix.  """  
      self.EnableCPayLegal:bool = obj["EnableCPayLegal"]
      """  Flag to indicate when to enable the CPay Legal Number combo  """  
      self.DispCPayParent:bool = obj["DispCPayParent"]
      """  Flag to indicate if the External Company is the Central Payment Parent Company.  """  
      self.EnableARIntercompany:bool = obj["EnableARIntercompany"]
      """  Flag to indicate when to enable the AR Intercompany Account button.  """  
      self.ExtSystemExtSystemName:str = obj["ExtSystemExtSystemName"]
      """  Full Name of external package  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.LinkCustomerBTName:str = obj["LinkCustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.LinkCustomerCustID:str = obj["LinkCustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.LinkCustomerName:str = obj["LinkCustomerName"]
      """  The full name of the customer.  """  
      self.LinkVendorAddress1:str = obj["LinkVendorAddress1"]
      """  First address line of the Supplier  """  
      self.LinkVendorCity:str = obj["LinkVendorCity"]
      """  City portion of the address of the Supplier  """  
      self.LinkVendorDefaultFOB:str = obj["LinkVendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.LinkVendorTermsCode:str = obj["LinkVendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.LinkVendorAddress2:str = obj["LinkVendorAddress2"]
      """  Second address line of the Supplier  """  
      self.LinkVendorCountry:str = obj["LinkVendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.LinkVendorName:str = obj["LinkVendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.LinkVendorVendorID:str = obj["LinkVendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.LinkVendorAddress3:str = obj["LinkVendorAddress3"]
      """  Third address line of the Supplier  """  
      self.LinkVendorCurrencyCode:str = obj["LinkVendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LinkVendorState:str = obj["LinkVendorState"]
      """  Can be blank.  """  
      self.LinkVendorZIP:str = obj["LinkVendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyListTableset:
   def __init__(self, obj):
      self.ExtCompanyList:list[Erp_Tablesets_ExtCompanyListRow] = obj["ExtCompanyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ExtCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.CompanyCountryLangNameID:str = obj["CompanyCountryLangNameID"]
      """  CompanyCountryLangNameID  """  
      self.SendCustomer:bool = obj["SendCustomer"]
      """  Customers will be sent . CustomerType = "CUS". Init YES  """  
      self.SendProspect:bool = obj["SendProspect"]
      """  Prospects will be sent . CustomerType = "PRO". Init YES  """  
      self.SendSuspect:bool = obj["SendSuspect"]
      """  Suspects  will be sent. CustomerType = "SUS". Init NO  """  
      self.SendVend:bool = obj["SendVend"]
      """  Vendors will be sent .  Init YES  """  
      self.SendPart:bool = obj["SendPart"]
      """  Parts will be sent.  Init NO (Future USE)  """  
      self.SendShip:bool = obj["SendShip"]
      """  Shipments will be sent .  Init YES  """  
      self.SendARInv:bool = obj["SendARInv"]
      """  AR Invoices will be sent .  Init YES  """  
      self.RcvARInv:bool = obj["RcvARInv"]
      """  AR Invoices will be received .  Init YES  """  
      self.SendAPInv:bool = obj["SendAPInv"]
      """  AP Invoices will be sent .  Init YES  """  
      self.RcvAPInv:bool = obj["RcvAPInv"]
      """  AP Invoices will be received .  Init YES  """  
      self.APPurchType:bool = obj["APPurchType"]
      """  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  """  
      self.SendAckToQue:bool = obj["SendAckToQue"]
      """  For this interface, should acknowledgments be sent back to the interfaced software when a record is received into the intermediate tables?  """  
      self.ICTrading:bool = obj["ICTrading"]
      """  Indicates if this external company setup supports Inter-Company Trading.  """  
      self.ICVendorNum:int = obj["ICVendorNum"]
      """  A  unique integer assigned by the system to identify the Vendor participating in the Inter-Company Trading.  """  
      self.ICCustNum:int = obj["ICCustNum"]
      """  A  unique integer assigned by the system to identify the Customer participating in the Inter-Company Trading.  """  
      self.ExtCustID:str = obj["ExtCustID"]
      """  A user defined external customer ID.  Identifies the External Customer participating in the Inter-Company Trading.  """  
      self.ExtVendorID:str = obj["ExtVendorID"]
      """  A user defined external vendor ID.  Identifies the External Vendor participating in the Inter-Company Trading.  """  
      self.APDiscount:bool = obj["APDiscount"]
      """  Indicates that the discount amount by line needs to be captured to be sent to the Financials package  """  
      self.AuxPrgmType:str = obj["AuxPrgmType"]
      """  The type of program being called (ProgressProgram or WindowsProgram)  """  
      self.AuxPrgmName:str = obj["AuxPrgmName"]
      """  Name of Auxiliary program to run to alert external system that there are records ready for processing  """  
      self.SendPOSugg:bool = obj["SendPOSugg"]
      """  New PO Suggestions will be sent.  """  
      self.LastConDate:str = obj["LastConDate"]
      """  Last date the connection was made successfully  """  
      self.LastConTime:int = obj["LastConTime"]
      """  Last Time the connection was made successfully  """  
      self.LastFailedDate:str = obj["LastFailedDate"]
      """  last date the connection was attempted and failed  """  
      self.LastFailedTime:int = obj["LastFailedTime"]
      """  Last time the connection was tried and failed  """  
      self.TransferDays:int = obj["TransferDays"]
      """  Number of days it will take to transfer an order from one company to the other.  Only for Inter-Company traders.  Will subtract this number from the po need by date to get the correct need by date on the order side.  Controlled on the Order side (po due-date - transfertime = orderdate)  """  
      self.PONumBlockSize:int = obj["PONumBlockSize"]
      """  Size of blocks for POHeader.PONum to be generated for this Consolidated Purchasing Company.  """  
      self.PONumBlockReorderPoint:int = obj["PONumBlockReorderPoint"]
      """  When a Consolidated Purchasing Company requests a new block because their portion of their POHeader.PONum block is less than this Reorder Point, create a new block and send it out.  """  
      self.PONumBlockWarnPoint:int = obj["PONumBlockWarnPoint"]
      """  When a Consolidated Purchasing Company creates a Purchase Order and the number of allocated PONum values drops below this warning point, message the user to inform them.  """  
      self.DefaultPlant:str = obj["DefaultPlant"]
      """  Establishes the default ExtSite.ExtSiteID to be used as the default for a Site field during creation of a Consolidated Purchase Order Release.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SendGLAccounts:bool = obj["SendGLAccounts"]
      """  Send G/L Accounts for Multi-Company Journal.  """  
      self.AllowGJAlloc:bool = obj["AllowGJAlloc"]
      """  Indicates if the current company is allowed to send Multi-Company General Journals to this external company.  """  
      self.AllowAPAlloc:bool = obj["AllowAPAlloc"]
      """  Indicates if the current company is allowed to send Multi-Company AP G/L entries to this external company.  """  
      self.JrnGroupPrefix:str = obj["JrnGroupPrefix"]
      """  The Journal Group prefix to use when determining the group ID for the Multi-Company Journals coming from this external company.  """  
      self.AutoPostGJ:bool = obj["AutoPostGJ"]
      """  Flag to indicate if the Multi-Company Journals coming from this external company needs to be posted automatically.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The Journal Code to use to enter Multi-Company Journals from this external company.  """  
      self.CPayGroupPrefix:str = obj["CPayGroupPrefix"]
      """  The default Invoice Group Prefix that will be used by Centralized Payment process.  """  
      self.CPayAutoPost:bool = obj["CPayAutoPost"]
      """  The flag to indicate if invoices flagged for Centralized Payment from external company will be posted automatically.  """  
      self.CPayLegalNum:str = obj["CPayLegalNum"]
      """   This field will indicate how Legal Number will be generated.  The valid options are:
'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 
'N'  -  Generate New Legal Number using the current company's Legal Number rules.  """  
      self.AutoLoadCust:bool = obj["AutoLoadCust"]
      """  When receiving global customers, try to create/link the Part without human intervention  """  
      self.AutoLoadVend:bool = obj["AutoLoadVend"]
      """  When receiving global vendors, try to create/link a vendor without human intervention  """  
      self.AutoLoadPart:bool = obj["AutoLoadPart"]
      """  When receiving Global Parts, try to create/link a Part without human intervention  """  
      self.SendRev:bool = obj["SendRev"]
      """  Part revisions will be sent.  Init NO (Future USE)  """  
      self.SendPerCon:bool = obj["SendPerCon"]
      """  PerCon will be sent.  """  
      self.MCSegOnly:bool = obj["MCSegOnly"]
      """  MCSegOnly  """  
      self.SendConfigurator:bool = obj["SendConfigurator"]
      """  SendConfigurator  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendGlobalCOA:bool = obj["SendGlobalCOA"]
      """  Turns Global COA on  """  
      self.SendGlobalCOAType:str = obj["SendGlobalCOAType"]
      """  Indicates how much of the COA supporting structure to send. seg`Send Segments Only~coa`Send Full COA  """  
      self.AlwaysUseGLInterComp:bool = obj["AlwaysUseGLInterComp"]
      """  It is used for rules of creation offsetting GL inter-company lines in multi-company process. If it is checked the journal will have an offsetting line with inter-company account for each multi-company line.  """  
      self.CColGroupPrefix:str = obj["CColGroupPrefix"]
      """  The default Invoice Group Prefix that will be used by Centralized Collection process.  """  
      self.CColCPayLegalNum:str = obj["CColCPayLegalNum"]
      """  This field will indicate how Legal Number will be generated for Central Collection invoices.  The valid options are: 'O'  -  Use Original Legal Number from the source invoice prefixed with the Source Company ID; 'N'  -  Generate New Legal Number using the current company's Legal Number rules.  """  
      self.SendDynAttr:bool = obj["SendDynAttr"]
      """  Dynamic Attributes will be sent.  Init NO  """  
      self.RcvDynAttr:bool = obj["RcvDynAttr"]
      """  Dynamic Attributes will be received.  Init NO  """  
      self.DispCPayParent:bool = obj["DispCPayParent"]
      """  Flag to indicate if the External Company is the Central Payment Parent Company.  """  
      self.EnableARIntercompany:bool = obj["EnableARIntercompany"]
      """  Flag to indicate when to enable the AR Intercompany Account button.  """  
      self.EnableConvertToDirect:bool = obj["EnableConvertToDirect"]
      self.EnableConvertToSonic:bool = obj["EnableConvertToSonic"]
      self.EnableCPayGroup:bool = obj["EnableCPayGroup"]
      """  Flag to indicate when to enable the CPay Group Prefix.  """  
      self.EnableCPayLegal:bool = obj["EnableCPayLegal"]
      """  Flag to indicate when to enable the CPay Legal Number combo  """  
      self.ExtCompanyName:str = obj["ExtCompanyName"]
      """  Name or description of the external company.  """  
      self.ExtSystemIDTransferMethod:str = obj["ExtSystemIDTransferMethod"]
      self.AllowAPPurchType:bool = obj["AllowAPPurchType"]
      self.EnableCColCPayLegalNum:bool = obj["EnableCColCPayLegalNum"]
      """  Flag to indicate when to enable the Central Collection Legal Number  """  
      self.EnableCColGroupPrefix:bool = obj["EnableCColGroupPrefix"]
      """  Flag to indicate when to enable the Central Collection Group Prefix.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ExtSystemExtSystemName:str = obj["ExtSystemExtSystemName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.LinkCustomerName:str = obj["LinkCustomerName"]
      self.LinkCustomerBTName:str = obj["LinkCustomerBTName"]
      self.LinkCustomerCustID:str = obj["LinkCustomerCustID"]
      self.LinkCustomerInactive:bool = obj["LinkCustomerInactive"]
      self.LinkVendorAddress1:str = obj["LinkVendorAddress1"]
      self.LinkVendorCity:str = obj["LinkVendorCity"]
      self.LinkVendorDefaultFOB:str = obj["LinkVendorDefaultFOB"]
      self.LinkVendorTermsCode:str = obj["LinkVendorTermsCode"]
      self.LinkVendorAddress2:str = obj["LinkVendorAddress2"]
      self.LinkVendorCountry:str = obj["LinkVendorCountry"]
      self.LinkVendorName:str = obj["LinkVendorName"]
      self.LinkVendorVendorID:str = obj["LinkVendorVendorID"]
      self.LinkVendorAddress3:str = obj["LinkVendorAddress3"]
      self.LinkVendorCurrencyCode:str = obj["LinkVendorCurrencyCode"]
      self.LinkVendorState:str = obj["LinkVendorState"]
      self.LinkVendorZIP:str = obj["LinkVendorZIP"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTableset:
   def __init__(self, obj):
      self.ExtCompany:list[Erp_Tablesets_ExtCompanyRow] = obj["ExtCompany"]
      self.ExtCompanyAttch:list[Erp_Tablesets_ExtCompanyAttchRow] = obj["ExtCompanyAttch"]
      self.ExtCompanyECC:list[Erp_Tablesets_ExtCompanyECCRow] = obj["ExtCompanyECC"]
      self.ECCDocType:list[Erp_Tablesets_ECCDocTypeRow] = obj["ECCDocType"]
      self.ECCReportDefaultStyle:list[Erp_Tablesets_ECCReportDefaultStyleRow] = obj["ECCReportDefaultStyle"]
      self.ExtPlant:list[Erp_Tablesets_ExtPlantRow] = obj["ExtPlant"]
      self.ExtWarehouse:list[Erp_Tablesets_ExtWarehouseRow] = obj["ExtWarehouse"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtCompanyTriggerDef:list[Erp_Tablesets_ExtCompanyTriggerDefRow] = obj["ExtCompanyTriggerDef"]
      self.ExtCompanyTriggerConditionGrp:list[Erp_Tablesets_ExtCompanyTriggerConditionGrpRow] = obj["ExtCompanyTriggerConditionGrp"]
      self.ExtCompanyTriggerAction:list[Erp_Tablesets_ExtCompanyTriggerActionRow] = obj["ExtCompanyTriggerAction"]
      self.ExtCompanyTriggerCondition:list[Erp_Tablesets_ExtCompanyTriggerConditionRow] = obj["ExtCompanyTriggerCondition"]
      self.ExtCompanyTriggerConditionData:list[Erp_Tablesets_ExtCompanyTriggerConditionDataRow] = obj["ExtCompanyTriggerConditionData"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ExtCompanyTriggerActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.TriggerActionNum:int = obj["TriggerActionNum"]
      """  TriggerActionNum  """  
      self.ActionType:str = obj["ActionType"]
      """  ActionType  """  
      self.WorkflowName:str = obj["WorkflowName"]
      """  WorkflowName  """  
      self.ActionIsAsynchronous:bool = obj["ActionIsAsynchronous"]
      """  ActionIsAsynchronous  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerConditionDataRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.TriggerConditionGroupNum:int = obj["TriggerConditionGroupNum"]
      """  TriggerConditionGroupNum  """  
      self.TriggerConditionNum:int = obj["TriggerConditionNum"]
      """  TriggerConditionNum  """  
      self.TriggerConditionDataNum:int = obj["TriggerConditionDataNum"]
      """  TriggerConditionDataNum  """  
      self.Data:str = obj["Data"]
      """  Data  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerConditionGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.TriggerConditionGroupNum:int = obj["TriggerConditionGroupNum"]
      """  TriggerConditionGroupNum  """  
      self.TriggerActionNum:int = obj["TriggerActionNum"]
      """  TriggerActionNum  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerConditionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.TriggerConditionGroupNum:int = obj["TriggerConditionGroupNum"]
      """  TriggerConditionGroupNum  """  
      self.TriggerConditionNum:int = obj["TriggerConditionNum"]
      """  TriggerConditionNum  """  
      self.OrderSeq:int = obj["OrderSeq"]
      """  OrderSeq  """  
      self.Operator:str = obj["Operator"]
      """  Operator  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.ConditionTypeName:str = obj["ConditionTypeName"]
      """  ConditionTypeName  """  
      self.Postfix:str = obj["Postfix"]
      """  Postfix  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.Data:str = obj["Data"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtCompanyTriggerDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  DBTableName  """  
      self.TriggerType:str = obj["TriggerType"]
      """  TriggerType  """  
      self.IsEnabled:bool = obj["IsEnabled"]
      """  IsEnabled  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.ExtCompCharacter01:str = obj["ExtCompCharacter01"]
      """  ExtCompCharacter01  """  
      self.ExtCompCharacter02:str = obj["ExtCompCharacter02"]
      """  ExtCompCharacter02  """  
      self.ExtCompBoolean01:bool = obj["ExtCompBoolean01"]
      """  ExtCompBoolean01  """  
      self.ExtCompBoolean02:bool = obj["ExtCompBoolean02"]
      """  ExtCompBoolean02  """  
      self.ExtCompDateTime01:str = obj["ExtCompDateTime01"]
      """  ExtCompDateTime01  """  
      self.ExtCompDateTime02:str = obj["ExtCompDateTime02"]
      """  ExtCompDateTime02  """  
      self.ExtCompInteger01:int = obj["ExtCompInteger01"]
      """  ExtCompInteger01  """  
      self.ExtCompInteger02:int = obj["ExtCompInteger02"]
      """  ExtCompInteger02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DeveloperMode:bool = obj["DeveloperMode"]
      self.IsUpdatable:bool = obj["IsUpdatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.ExtPlantID:str = obj["ExtPlantID"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Main phone number of the Site.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Main fax number of the Site.  """  
      self.DefaultWhse:str = obj["DefaultWhse"]
      """  ExtWarehouse.ExtWarehouseID as the default external warehouse for this external Site.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtWarehouseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtPlantID:str = obj["ExtPlantID"]
      """  Unique identifier of this external Site assigned by the user.  """  
      self.ExtWarehouseID:str = obj["ExtWarehouseID"]
      """  Unique identifier of this warehouse assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtExtCompanyTableset:
   def __init__(self, obj):
      self.ExtCompany:list[Erp_Tablesets_ExtCompanyRow] = obj["ExtCompany"]
      self.ExtCompanyAttch:list[Erp_Tablesets_ExtCompanyAttchRow] = obj["ExtCompanyAttch"]
      self.ExtCompanyECC:list[Erp_Tablesets_ExtCompanyECCRow] = obj["ExtCompanyECC"]
      self.ECCDocType:list[Erp_Tablesets_ECCDocTypeRow] = obj["ECCDocType"]
      self.ECCReportDefaultStyle:list[Erp_Tablesets_ECCReportDefaultStyleRow] = obj["ECCReportDefaultStyle"]
      self.ExtPlant:list[Erp_Tablesets_ExtPlantRow] = obj["ExtPlant"]
      self.ExtWarehouse:list[Erp_Tablesets_ExtWarehouseRow] = obj["ExtWarehouse"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtCompanyTriggerDef:list[Erp_Tablesets_ExtCompanyTriggerDefRow] = obj["ExtCompanyTriggerDef"]
      self.ExtCompanyTriggerConditionGrp:list[Erp_Tablesets_ExtCompanyTriggerConditionGrpRow] = obj["ExtCompanyTriggerConditionGrp"]
      self.ExtCompanyTriggerAction:list[Erp_Tablesets_ExtCompanyTriggerActionRow] = obj["ExtCompanyTriggerAction"]
      self.ExtCompanyTriggerCondition:list[Erp_Tablesets_ExtCompanyTriggerConditionRow] = obj["ExtCompanyTriggerCondition"]
      self.ExtCompanyTriggerConditionData:list[Erp_Tablesets_ExtCompanyTriggerConditionDataRow] = obj["ExtCompanyTriggerConditionData"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FSA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.disabledList:str = obj["parameters"]
      self.checkedList:str = obj["parameters"]
      pass

      """  output parameters  """  

class Generic_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.disabledList:str = obj["parameters"]
      self.checkedList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   extSystemID
   extCompanyID
   """  
   def __init__(self, obj):
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtCompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtCompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtCompanyTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetECCReportServiceDescList_output:
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
      self.returnObj:list[Erp_Tablesets_ExtCompanyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewECCDocType_input:
   """ Required : 
   ds
   extCompanyID
   extSystemID
   ecCID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.extSystemID:str = obj["extSystemID"]
      self.ecCID:int = obj["ecCID"]
      pass

class GetNewECCDocType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECCReportDefaultStyle_input:
   """ Required : 
   ds
   extCompanyID
   extSystemID
   ecCID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.extSystemID:str = obj["extSystemID"]
      self.ecCID:int = obj["ecCID"]
      pass

class GetNewECCReportDefaultStyle_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtCompanyAttch_input:
   """ Required : 
   ds
   extSystemID
   extCompanyID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class GetNewExtCompanyAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtCompanyECC_input:
   """ Required : 
   ds
   extCompanyID
   extSystemID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.extSystemID:str = obj["extSystemID"]
      pass

class GetNewExtCompanyECC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtCompanyTriggerAction_input:
   """ Required : 
   ds
   extSystemID
   extCompanyID
   schemaName
   dbTableName
   triggerType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.schemaName:str = obj["schemaName"]
      self.dbTableName:str = obj["dbTableName"]
      self.triggerType:str = obj["triggerType"]
      pass

class GetNewExtCompanyTriggerAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtCompanyTriggerConditionData_input:
   """ Required : 
   ds
   extSystemID
   extCompanyID
   schemaName
   dbTableName
   triggerType
   triggerConditionGroupNum
   triggerConditionNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.schemaName:str = obj["schemaName"]
      self.dbTableName:str = obj["dbTableName"]
      self.triggerType:str = obj["triggerType"]
      self.triggerConditionGroupNum:int = obj["triggerConditionGroupNum"]
      self.triggerConditionNum:int = obj["triggerConditionNum"]
      pass

class GetNewExtCompanyTriggerConditionData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtCompanyTriggerConditionGrp_input:
   """ Required : 
   ds
   extSystemID
   extCompanyID
   schemaName
   dbTableName
   triggerType
   triggerConditionGroupNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.schemaName:str = obj["schemaName"]
      self.dbTableName:str = obj["dbTableName"]
      self.triggerType:str = obj["triggerType"]
      self.triggerConditionGroupNum:int = obj["triggerConditionGroupNum"]
      pass

class GetNewExtCompanyTriggerConditionGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtCompanyTriggerCondition_input:
   """ Required : 
   ds
   extSystemID
   extCompanyID
   schemaName
   dbTableName
   triggerType
   triggerConditionGroupNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.schemaName:str = obj["schemaName"]
      self.dbTableName:str = obj["dbTableName"]
      self.triggerType:str = obj["triggerType"]
      self.triggerConditionGroupNum:int = obj["triggerConditionGroupNum"]
      pass

class GetNewExtCompanyTriggerCondition_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtCompanyTriggerDef_input:
   """ Required : 
   ds
   extSystemID
   extCompanyID
   schemaName
   dbTableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.schemaName:str = obj["schemaName"]
      self.dbTableName:str = obj["dbTableName"]
      pass

class GetNewExtCompanyTriggerDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtCompany_input:
   """ Required : 
   ds
   extSystemID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      pass

class GetNewExtCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtPlant_input:
   """ Required : 
   ds
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class GetNewExtPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtWarehouse_input:
   """ Required : 
   ds
   extSystemID
   transferMethod
   extCompanyID
   extPlantID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.extPlantID:str = obj["extPlantID"]
      pass

class GetNewExtWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseExtCompany
   whereClauseExtCompanyAttch
   whereClauseExtCompanyECC
   whereClauseECCDocType
   whereClauseECCReportDefaultStyle
   whereClauseExtPlant
   whereClauseExtWarehouse
   whereClauseEntityGLC
   whereClauseExtCompanyTriggerDef
   whereClauseExtCompanyTriggerConditionGrp
   whereClauseExtCompanyTriggerAction
   whereClauseExtCompanyTriggerCondition
   whereClauseExtCompanyTriggerConditionData
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseExtCompany:str = obj["whereClauseExtCompany"]
      self.whereClauseExtCompanyAttch:str = obj["whereClauseExtCompanyAttch"]
      self.whereClauseExtCompanyECC:str = obj["whereClauseExtCompanyECC"]
      self.whereClauseECCDocType:str = obj["whereClauseECCDocType"]
      self.whereClauseECCReportDefaultStyle:str = obj["whereClauseECCReportDefaultStyle"]
      self.whereClauseExtPlant:str = obj["whereClauseExtPlant"]
      self.whereClauseExtWarehouse:str = obj["whereClauseExtWarehouse"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClauseExtCompanyTriggerDef:str = obj["whereClauseExtCompanyTriggerDef"]
      self.whereClauseExtCompanyTriggerConditionGrp:str = obj["whereClauseExtCompanyTriggerConditionGrp"]
      self.whereClauseExtCompanyTriggerAction:str = obj["whereClauseExtCompanyTriggerAction"]
      self.whereClauseExtCompanyTriggerCondition:str = obj["whereClauseExtCompanyTriggerCondition"]
      self.whereClauseExtCompanyTriggerConditionData:str = obj["whereClauseExtCompanyTriggerConditionData"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtCompanyTableset] = obj["returnObj"]
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

class InitCOA_input:
   """ Required : 
   extCompanyID
   extTransferMethod
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      """  The External Company ID  """  
      self.extTransferMethod:str = obj["extTransferMethod"]
      """  The external Company transfer method  """  
      pass

class InitCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errlog:str = obj["parameters"]
      pass

      """  output parameters  """  

class InitConsolidationMonitor_input:
   """ Required : 
   extCompanyID
   extTransferMethod
   fromDate
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      """  The External Company ID  """  
      self.extTransferMethod:str = obj["extTransferMethod"]
      """  The external Company transfer method  """  
      self.fromDate:str = obj["fromDate"]
      """  Filter to skip old consolidations  """  
      pass

class InitConsolidationMonitor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errlog:str = obj["parameters"]
      pass

      """  output parameters  """  

class InitEntprsConf_input:
   """ Required : 
   extCompanyID
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      """  The External Company ID  """  
      pass

class InitEntprsConf_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errlog:str = obj["parameters"]
      pass

      """  output parameters  """  

class InitMultiCompany_input:
   """ Required : 
   extCompanyID
   extTransferMethod
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      """  The External Company ID  """  
      self.extTransferMethod:str = obj["extTransferMethod"]
      """  The external Company transfer method  """  
      pass

class InitMultiCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errlog:str = obj["parameters"]
      pass

      """  output parameters  """  

class Mobile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.disabledList:str = obj["parameters"]
      self.checkedList:str = obj["parameters"]
      pass

      """  output parameters  """  

class MultiCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.disabledList:str = obj["parameters"]
      self.checkedList:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeECCSiteName_input:
   """ Required : 
   eccSiteName
   """  
   def __init__(self, obj):
      self.eccSiteName:str = obj["eccSiteName"]
      pass

class OnChangeECCSiteName_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeLocation_input:
   """ Required : 
   proposedLocation
   proposedTableName
   """  
   def __init__(self, obj):
      self.proposedLocation:str = obj["proposedLocation"]
      self.proposedTableName:str = obj["proposedTableName"]
      pass

class OnChangeLocation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inSchema:str = obj["parameters"]
      self.outSchema:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeTriggerDefTableName_input:
   """ Required : 
   proposedTableName
   ds
   """  
   def __init__(self, obj):
      self.proposedTableName:str = obj["proposedTableName"]
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

class OnChangeTriggerDefTableName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PLM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.disabledList:str = obj["parameters"]
      self.checkedList:str = obj["parameters"]
      pass

      """  output parameters  """  

class SupplierConnect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.disabledList:str = obj["parameters"]
      self.checkedList:str = obj["parameters"]
      pass

      """  output parameters  """  

class TestConnection_input:
   """ Required : 
   extCompRowid
   """  
   def __init__(self, obj):
      self.extCompRowid:str = obj["extCompRowid"]
      """  The RowIdent of the record of which to test connection  """  
      pass

class TestConnection_output:
   def __init__(self, obj):
      pass

class TestECCConnection_input:
   """ Required : 
   extCompRowid
   """  
   def __init__(self, obj):
      self.extCompRowid:str = obj["extCompRowid"]
      pass

class TestECCConnection_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.msgConnection:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtCompanyTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtCompanyTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateReportService_input:
   """ Required : 
   extCompanyID
   extsystemID
   eccID
   autoProgram
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      """  extCompanyID  """  
      self.extsystemID:str = obj["extsystemID"]
      """  extsystemID  """  
      self.eccID:int = obj["eccID"]
      """  eccID  """  
      self.autoProgram:str = obj["autoProgram"]
      """  Report Service  """  
      pass

class ValidateReportService_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class WriteXSDSchemasToServer_input:
   """ Required : 
   proposedLocation
   specialFolder
   proposedTableName
   """  
   def __init__(self, obj):
      self.proposedLocation:str = obj["proposedLocation"]
      """  relative path on the server  """  
      self.specialFolder:int = obj["specialFolder"]
      """  the type of the folder location (Report, UserData, Company Data and so on)  """  
      self.proposedTableName:str = obj["proposedTableName"]
      """  The name of the table  """  
      pass

class WriteXSDSchemasToServer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inSchemaFileName:str = obj["parameters"]
      self.outSchemaFileName:str = obj["parameters"]
      pass

      """  output parameters  """  

