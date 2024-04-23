import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLBCOASvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOAs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBCOAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOAs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs",headers=creds) as resp:
           return await resp.json()

async def post_GLBCOAs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOAs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBCOARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBCOAs_Company_ExtCompanyID_COACode(Company, ExtCompanyID, COACode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOA item
   Description: Calls GetByID to retrieve the GLBCOA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBCOAs_Company_ExtCompanyID_COACode(Company, ExtCompanyID, COACode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBCOA for the service
   Description: Calls UpdateExt to update GLBCOA. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBCOAs_Company_ExtCompanyID_COACode(Company, ExtCompanyID, COACode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBCOA item
   Description: Call UpdateExt to delete GLBCOA item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOAs_Company_ExtCompanyID_COACode_GLBCOASegments(Company, ExtCompanyID, COACode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLBCOASegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBCOASegments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")/GLBCOASegments",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOAs_Company_ExtCompanyID_COACode_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOASegment item
   Description: Calls GetByID to retrieve the GLBCOASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegments(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBCOASegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegments
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments",headers=creds) as resp:
           return await resp.json()

async def post_GLBCOASegments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOASegment item
   Description: Calls GetByID to retrieve the GLBCOASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBCOASegment for the service
   Description: Calls UpdateExt to update GLBCOASegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBCOASegment item
   Description: Call UpdateExt to delete GLBCOASegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr_GLBCOASegValues(Company, ExtCompanyID, COACode, SegmentNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLBCOASegValues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBCOASegValues1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")/GLBCOASegValues",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOASegValue item
   Description: Calls GetByID to retrieve the GLBCOASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegValue1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBCOASegValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues",headers=creds) as resp:
           return await resp.json()

async def post_GLBCOASegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOASegValue item
   Description: Calls GetByID to retrieve the GLBCOASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBCOASegValue for the service
   Description: Calls UpdateExt to update GLBCOASegValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBCOASegValue item
   Description: Call UpdateExt to delete GLBCOASegValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOAListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLBCOA, whereClauseGLBCOASegment, whereClauseGLBCOASegValues, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLBCOA=" + whereClauseGLBCOA
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLBCOASegment=" + whereClauseGLBCOASegment
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLBCOASegValues=" + whereClauseGLBCOASegValues
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extCompanyID, coACode, epicorHeaders = None):
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
   params += "extCompanyID=" + extCompanyID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "coACode=" + coACode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBCOA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBCOASegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBCOASegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBCOASegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBCOASegValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOAListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOAListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOASegValuesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOASegmentRow] = obj["value"]
      pass

class Erp_Tablesets_GLBCOAListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Identifieds the COA as one that is sent to the External Companies for GL processing.  If the ExtCompID is not null this field must be No.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Identifieds the COA as one that is sent to the External Companies for GL processing.  If the ExtCompID is not null this field must be No.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  GlobalCOA  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  RebuildGLAccts  """  
      self.PESunatCOA:str = obj["PESunatCOA"]
      """  Peru CSF: SUNAT Chart of Accounts Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  ReverseCategory  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  ExtAnalysisCode  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.BENAEID:str = obj["BENAEID"]
      """  BENAEID  """  
      self.Mapped:bool = obj["Mapped"]
      """  Mapped  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  ReportCategory  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  LinkedPlant  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.MaxLength:int = obj["MaxLength"]
      """  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  """  
      self.MinLength:int = obj["MinLength"]
      """  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  """  
      self.Dynamic:bool = obj["Dynamic"]
      """  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  """  
      self.UseRefEntity:bool = obj["UseRefEntity"]
      """  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  """  
      self.AllowAlpha:bool = obj["AllowAlpha"]
      """  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  """  
      self.EntryControl:str = obj["EntryControl"]
      """  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  """  
      self.SegSelfBal:bool = obj["SegSelfBal"]
      """  Indicates if journal entries are automatically balanced.  """  
      self.Level:int = obj["Level"]
      """  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  """  
      self.SummaryBal:bool = obj["SummaryBal"]
      """  Indicates if this segment is included in the standard trial balance account.  """  
      self.DetailBal:bool = obj["DetailBal"]
      """  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  """  
      self.KeepOpenBal:bool = obj["KeepOpenBal"]
      """  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  """  
      self.AutoCreateSegVals:bool = obj["AutoCreateSegVals"]
      """  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  """  
      self.SelfBalAcct:str = obj["SelfBalAcct"]
      """  Account used  when creating balancing transactions for this segment.  """  
      self.BalSegValue1:str = obj["BalSegValue1"]
      """  Balance Seg Value 1  """  
      self.BalSegValue2:str = obj["BalSegValue2"]
      """  Balance Seg Value 2  """  
      self.BalSegValue3:str = obj["BalSegValue3"]
      """  Balance Seg Value 3  """  
      self.BalSegValue4:str = obj["BalSegValue4"]
      """  Balance Seg Value 4  """  
      self.BalSegValue5:str = obj["BalSegValue5"]
      """  Balance Seg Value 5  """  
      self.BalSegValue6:str = obj["BalSegValue6"]
      """  Balance Seg Value 6  """  
      self.BalSegValue7:str = obj["BalSegValue7"]
      """  Balance Seg Value 7  """  
      self.BalSegValue8:str = obj["BalSegValue8"]
      """  Balance Seg Value 8  """  
      self.BalSegValue9:str = obj["BalSegValue9"]
      """  Balance Seg Value 9  """  
      self.BalSegValue10:str = obj["BalSegValue10"]
      """  Balance Seg Value 10  """  
      self.BalSegValue11:str = obj["BalSegValue11"]
      """  Balance Seg Value 11  """  
      self.BalSegValue12:str = obj["BalSegValue12"]
      """  Balance Seg Value 12  """  
      self.BalSegValue13:str = obj["BalSegValue13"]
      """  Balance Seg Value 13  """  
      self.BalSegValue14:str = obj["BalSegValue14"]
      """  Balance Seg Value 14  """  
      self.BalSegValue15:str = obj["BalSegValue15"]
      """  Balance Seg Value 15  """  
      self.BalSegValue16:str = obj["BalSegValue16"]
      """  Balance Seg Value 16  """  
      self.BalSegValue17:str = obj["BalSegValue17"]
      """  Balance Seg Value 17  """  
      self.BalSegValue18:str = obj["BalSegValue18"]
      """  Balance Seg Value 18  """  
      self.BalSegValue19:str = obj["BalSegValue19"]
      """  Balance Seg Value 19  """  
      self.BalSegValue20:str = obj["BalSegValue20"]
      """  Balance Seg Value 20  """  
      self.SelfOffAcct:str = obj["SelfOffAcct"]
      """  The Self Balance offset account used when balancing this segment.  """  
      self.OffSegValue1:str = obj["OffSegValue1"]
      """  Offset Segment Value 1  """  
      self.OffSegValue2:str = obj["OffSegValue2"]
      """  Offset Segment Value 2  """  
      self.OffSegValue3:str = obj["OffSegValue3"]
      """  Offset Segment Value 3  """  
      self.OffSegValue4:str = obj["OffSegValue4"]
      """  Offset Segment Value 4  """  
      self.OffSegValue5:str = obj["OffSegValue5"]
      """  Offset Segment Value 5  """  
      self.OffSegValue6:str = obj["OffSegValue6"]
      """  Offset Segment Value 6  """  
      self.OffSegValue7:str = obj["OffSegValue7"]
      """  Offset Segment Value 7  """  
      self.OffSegValue8:str = obj["OffSegValue8"]
      """  Offset Segment Value 8  """  
      self.OffSegValue9:str = obj["OffSegValue9"]
      """  Offset Segment Value 9  """  
      self.OffSegValue10:str = obj["OffSegValue10"]
      """  Offset Segment Value 10  """  
      self.OffSegValue11:str = obj["OffSegValue11"]
      """  Offset Segment Value 11  """  
      self.OffSegValue12:str = obj["OffSegValue12"]
      """  Offset Segment Value 12  """  
      self.OffSegValue13:str = obj["OffSegValue13"]
      """  Offset Segment Value 13  """  
      self.OffSegValue14:str = obj["OffSegValue14"]
      """  Offset Segment Value 14  """  
      self.OffSegValue15:str = obj["OffSegValue15"]
      """  Offset Segment Value 15  """  
      self.OffSegValue16:str = obj["OffSegValue16"]
      """  Offset Segment Value 16  """  
      self.OffSegValue17:str = obj["OffSegValue17"]
      """  Offset Segment Value 17  """  
      self.OffSegValue18:str = obj["OffSegValue18"]
      """  Offset Segment Value 18  """  
      self.OffSegValue19:str = obj["OffSegValue19"]
      """  Offset Segment Value 19  """  
      self.OffSegValue20:str = obj["OffSegValue20"]
      """  Offset Segment Value 20  """  
      self.ReverseCategoryID:str = obj["ReverseCategoryID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNIsCFICode:bool = obj["CNIsCFICode"]
      """  CNIsCFICode  """  
      self.SegValueField:str = obj["SegValueField"]
      """  SegValueField  """  
      self.DescFieldName:str = obj["DescFieldName"]
      """  DescFieldName  """  
      self.GlobalCOASegment:bool = obj["GlobalCOASegment"]
      """  GlobalCOASegment  """  
      self.GlobalCOASegmentValues:bool = obj["GlobalCOASegmentValues"]
      """  GlobalCOASegmentValues  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.GlobalValuesLock:bool = obj["GlobalValuesLock"]
      """  GlobalValuesLock  """  
      self.SiteSegment:bool = obj["SiteSegment"]
      """  SiteSegment  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   extCompanyID
   coACode
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLBCOAListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Identifieds the COA as one that is sent to the External Companies for GL processing.  If the ExtCompID is not null this field must be No.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOAListTableset:
   def __init__(self, obj):
      self.GLBCOAList:list[Erp_Tablesets_GLBCOAListRow] = obj["GLBCOAList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBCOARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Identifieds the COA as one that is sent to the External Companies for GL processing.  If the ExtCompID is not null this field must be No.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  GlobalCOA  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  RebuildGLAccts  """  
      self.PESunatCOA:str = obj["PESunatCOA"]
      """  Peru CSF: SUNAT Chart of Accounts Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  ReverseCategory  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  ExtAnalysisCode  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.BENAEID:str = obj["BENAEID"]
      """  BENAEID  """  
      self.Mapped:bool = obj["Mapped"]
      """  Mapped  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  ReportCategory  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  LinkedPlant  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.MaxLength:int = obj["MaxLength"]
      """  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  """  
      self.MinLength:int = obj["MinLength"]
      """  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  """  
      self.Dynamic:bool = obj["Dynamic"]
      """  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  """  
      self.UseRefEntity:bool = obj["UseRefEntity"]
      """  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  """  
      self.AllowAlpha:bool = obj["AllowAlpha"]
      """  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  """  
      self.EntryControl:str = obj["EntryControl"]
      """  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  """  
      self.SegSelfBal:bool = obj["SegSelfBal"]
      """  Indicates if journal entries are automatically balanced.  """  
      self.Level:int = obj["Level"]
      """  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  """  
      self.SummaryBal:bool = obj["SummaryBal"]
      """  Indicates if this segment is included in the standard trial balance account.  """  
      self.DetailBal:bool = obj["DetailBal"]
      """  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  """  
      self.KeepOpenBal:bool = obj["KeepOpenBal"]
      """  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  """  
      self.AutoCreateSegVals:bool = obj["AutoCreateSegVals"]
      """  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  """  
      self.SelfBalAcct:str = obj["SelfBalAcct"]
      """  Account used  when creating balancing transactions for this segment.  """  
      self.BalSegValue1:str = obj["BalSegValue1"]
      """  Balance Seg Value 1  """  
      self.BalSegValue2:str = obj["BalSegValue2"]
      """  Balance Seg Value 2  """  
      self.BalSegValue3:str = obj["BalSegValue3"]
      """  Balance Seg Value 3  """  
      self.BalSegValue4:str = obj["BalSegValue4"]
      """  Balance Seg Value 4  """  
      self.BalSegValue5:str = obj["BalSegValue5"]
      """  Balance Seg Value 5  """  
      self.BalSegValue6:str = obj["BalSegValue6"]
      """  Balance Seg Value 6  """  
      self.BalSegValue7:str = obj["BalSegValue7"]
      """  Balance Seg Value 7  """  
      self.BalSegValue8:str = obj["BalSegValue8"]
      """  Balance Seg Value 8  """  
      self.BalSegValue9:str = obj["BalSegValue9"]
      """  Balance Seg Value 9  """  
      self.BalSegValue10:str = obj["BalSegValue10"]
      """  Balance Seg Value 10  """  
      self.BalSegValue11:str = obj["BalSegValue11"]
      """  Balance Seg Value 11  """  
      self.BalSegValue12:str = obj["BalSegValue12"]
      """  Balance Seg Value 12  """  
      self.BalSegValue13:str = obj["BalSegValue13"]
      """  Balance Seg Value 13  """  
      self.BalSegValue14:str = obj["BalSegValue14"]
      """  Balance Seg Value 14  """  
      self.BalSegValue15:str = obj["BalSegValue15"]
      """  Balance Seg Value 15  """  
      self.BalSegValue16:str = obj["BalSegValue16"]
      """  Balance Seg Value 16  """  
      self.BalSegValue17:str = obj["BalSegValue17"]
      """  Balance Seg Value 17  """  
      self.BalSegValue18:str = obj["BalSegValue18"]
      """  Balance Seg Value 18  """  
      self.BalSegValue19:str = obj["BalSegValue19"]
      """  Balance Seg Value 19  """  
      self.BalSegValue20:str = obj["BalSegValue20"]
      """  Balance Seg Value 20  """  
      self.SelfOffAcct:str = obj["SelfOffAcct"]
      """  The Self Balance offset account used when balancing this segment.  """  
      self.OffSegValue1:str = obj["OffSegValue1"]
      """  Offset Segment Value 1  """  
      self.OffSegValue2:str = obj["OffSegValue2"]
      """  Offset Segment Value 2  """  
      self.OffSegValue3:str = obj["OffSegValue3"]
      """  Offset Segment Value 3  """  
      self.OffSegValue4:str = obj["OffSegValue4"]
      """  Offset Segment Value 4  """  
      self.OffSegValue5:str = obj["OffSegValue5"]
      """  Offset Segment Value 5  """  
      self.OffSegValue6:str = obj["OffSegValue6"]
      """  Offset Segment Value 6  """  
      self.OffSegValue7:str = obj["OffSegValue7"]
      """  Offset Segment Value 7  """  
      self.OffSegValue8:str = obj["OffSegValue8"]
      """  Offset Segment Value 8  """  
      self.OffSegValue9:str = obj["OffSegValue9"]
      """  Offset Segment Value 9  """  
      self.OffSegValue10:str = obj["OffSegValue10"]
      """  Offset Segment Value 10  """  
      self.OffSegValue11:str = obj["OffSegValue11"]
      """  Offset Segment Value 11  """  
      self.OffSegValue12:str = obj["OffSegValue12"]
      """  Offset Segment Value 12  """  
      self.OffSegValue13:str = obj["OffSegValue13"]
      """  Offset Segment Value 13  """  
      self.OffSegValue14:str = obj["OffSegValue14"]
      """  Offset Segment Value 14  """  
      self.OffSegValue15:str = obj["OffSegValue15"]
      """  Offset Segment Value 15  """  
      self.OffSegValue16:str = obj["OffSegValue16"]
      """  Offset Segment Value 16  """  
      self.OffSegValue17:str = obj["OffSegValue17"]
      """  Offset Segment Value 17  """  
      self.OffSegValue18:str = obj["OffSegValue18"]
      """  Offset Segment Value 18  """  
      self.OffSegValue19:str = obj["OffSegValue19"]
      """  Offset Segment Value 19  """  
      self.OffSegValue20:str = obj["OffSegValue20"]
      """  Offset Segment Value 20  """  
      self.ReverseCategoryID:str = obj["ReverseCategoryID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNIsCFICode:bool = obj["CNIsCFICode"]
      """  CNIsCFICode  """  
      self.SegValueField:str = obj["SegValueField"]
      """  SegValueField  """  
      self.DescFieldName:str = obj["DescFieldName"]
      """  DescFieldName  """  
      self.GlobalCOASegment:bool = obj["GlobalCOASegment"]
      """  GlobalCOASegment  """  
      self.GlobalCOASegmentValues:bool = obj["GlobalCOASegmentValues"]
      """  GlobalCOASegmentValues  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.GlobalValuesLock:bool = obj["GlobalValuesLock"]
      """  GlobalValuesLock  """  
      self.SiteSegment:bool = obj["SiteSegment"]
      """  SiteSegment  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOATableset:
   def __init__(self, obj):
      self.GLBCOA:list[Erp_Tablesets_GLBCOARow] = obj["GLBCOA"]
      self.GLBCOASegment:list[Erp_Tablesets_GLBCOASegmentRow] = obj["GLBCOASegment"]
      self.GLBCOASegValues:list[Erp_Tablesets_GLBCOASegValuesRow] = obj["GLBCOASegValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLBCOATableset:
   def __init__(self, obj):
      self.GLBCOA:list[Erp_Tablesets_GLBCOARow] = obj["GLBCOA"]
      self.GLBCOASegment:list[Erp_Tablesets_GLBCOASegmentRow] = obj["GLBCOASegment"]
      self.GLBCOASegValues:list[Erp_Tablesets_GLBCOASegValuesRow] = obj["GLBCOASegValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   extCompanyID
   coACode
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOATableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBCOATableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBCOATableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBCOAListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLBCOASegValues_input:
   """ Required : 
   ds
   extCompanyID
   coACode
   segmentNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOATableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      pass

class GetNewGLBCOASegValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOATableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLBCOASegment_input:
   """ Required : 
   ds
   extCompanyID
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOATableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewGLBCOASegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOATableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLBCOA_input:
   """ Required : 
   ds
   extCompanyID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOATableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class GetNewGLBCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOATableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLBCOA
   whereClauseGLBCOASegment
   whereClauseGLBCOASegValues
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLBCOA:str = obj["whereClauseGLBCOA"]
      self.whereClauseGLBCOASegment:str = obj["whereClauseGLBCOASegment"]
      self.whereClauseGLBCOASegValues:str = obj["whereClauseGLBCOASegValues"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOATableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGLBCOATableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBCOATableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOATableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOATableset] = obj["ds"]
      pass

      """  output parameters  """  

